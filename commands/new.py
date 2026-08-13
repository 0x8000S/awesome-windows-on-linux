# -*- coding: utf-8 -*-
"""new — 交互式创建新项目条目。

流程:
    1. 列出所有组（读取各组 metadata 的显示名），让用户选择。
    2. 让用户输入项目名（英文 ID，用于文件夹名与 name 字段）。
    3. 读取 project-meta 的语言基准（文件名集合），为该项目的每个语言
       生成对应的 JSON 模板文件。
"""
import os
import re
import sys

from core.config import FALLBACK_LANG
from core.scanner import collect, load_lang_file


# 项目名字符合法字符（用于文件夹名 / 作为 name 的默认值）
PROJECT_NAME_RE = re.compile(r"^[a-zA-Z0-9][a-zA-Z0-9\-_]*$")

# 生成的项目模板（必填字段留空，作者留空数组）
def _template(project_name, lang, primary_lang, supported_langs):
    return {
        "name": project_name,
        "intro": "",
        "restores": "",
        "license": "",
        "video": "",
        "url": "",
        "authors": [],
        "lang_primary": primary_lang,
        "lang_supported": supported_langs,
    }


def _ask_choice(prompt, count):
    while True:
        try:
            raw = input(prompt).strip()
        except (EOFError, KeyboardInterrupt):
            print("\n已取消")
            sys.exit(130)
        if raw == "":
            print("输入不能为空，请重试")
            continue
        try:
            idx = int(raw)
        except ValueError:
            print("请输入数字编号")
            continue
        if 1 <= idx <= count:
            return idx - 1
        print(f"编号超出范围（1-{count}）")


def _ask_project_name(prompt):
    while True:
        try:
            raw = input(prompt).strip()
        except (EOFError, KeyboardInterrupt):
            print("\n已取消")
            sys.exit(130)
        if not PROJECT_NAME_RE.match(raw):
            print("项目名只能含字母、数字、连字符、下划线，且不能以连字符/下划线开头")
            continue
        return raw


def run(base, verbose=True):
    collector = collect(base)

    # 1. 组列表
    groups = collector["groups"]
    if not groups:
        print("未发现任何组（project-datas/ 下没有组目录）")
        return 1

    print("可用组：")
    group_names = []
    for i, g in enumerate(groups):
        gm = load_lang_file([
            os.path.join(g["meta_dir"], f"{FALLBACK_LANG}.json"),
        ])
        disp = gm["name"] if gm and "name" in gm else g["id"]
        group_names.append(disp)
        print(f"  {i + 1}. {disp}")

    gi = _ask_choice("\n请选择组编号: ", len(groups))
    group = groups[gi]
    print(f"已选择组: {group_names[gi]}（目录 {group['id']}）")

    # 2. 项目名
    project_name = _ask_project_name("\n请输入项目名（英文 ID）: ")
    print(f"项目名: {project_name}")

    # 校验是否已存在同名项目
    for p in group["projects"]:
        if p["id"] == project_name:
            print(f"错误: 项目 '{project_name}' 已存在于组 {group['id']} 中")
            return 1

    # 3. 语言基准 = project-meta 文件名集合
    meta_langs = collector["meta"]["langs"]
    if not meta_langs:
        print("错误: project-meta/ 下没有任何语言文件，无法生成")
        return 1

    primary_lang = FALLBACK_LANG if FALLBACK_LANG in meta_langs else meta_langs[0]
    print(f"将按 project-meta 基准语言生成: {', '.join(meta_langs)}")

    # 4. 创建文件夹 + 各语言 JSON
    proj_dir = os.path.join(group["dir"], project_name)
    if os.path.exists(proj_dir):
        print(f"错误: 目录已存在 {proj_dir}")
        return 1
    os.makedirs(proj_dir)

    created = []
    for lang in meta_langs:
        fpath = os.path.join(proj_dir, f"{lang}.json")
        data = _template(project_name, lang, primary_lang, list(meta_langs))
        with open(fpath, "w", encoding="utf-8") as fh:
            import json
            json.dump(data, fh, ensure_ascii=False, indent=2)
            fh.write("\n")
        created.append(fpath)

    print("\n已创建项目条目：")
    for fpath in created:
        print(f"  {fpath}")

    print("\n下一步：")
    print("  1. 编辑刚生成的 JSON，填入 url / intro / restores / license / authors")
    print("  2. 运行 `python main.py generate` 重新生成 README")
    print("  3. 运行 `python main.py lint` 校验数据")
    return 0


def cmd(args):
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return run(base)
