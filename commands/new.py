# -*- coding: utf-8 -*-
"""new — 交互式创建新项目条目。

流程:
    1. 列出所有组（读取各组 metadata 的显示名），让用户选择。
    2. 让用户输入项目名（英文 ID，用于文件夹名与 name 字段）。
    3. 读取 project-meta 的语言基准（文件名集合），为该项目的每个语言
       生成对应的 JSON 模板文件。

交互提示语言默认按系统 locale 检测（detect_ui_lang），也支持通过
ui_lang 参数显式指定（zh-CN / en-US）。
"""
import json
import locale
import os
import re
import sys

from core.config import FALLBACK_LANG
from core.scanner import collect, load_lang_file

# 项目名字符合法字符（用于文件夹名 / 作为 name 的默认值）
PROJECT_NAME_RE = re.compile(r"^[a-zA-Z0-9][a-zA-Z0-9\-_]*$")


# 中英文文案
I18N = {
    "zh-CN": {
        "no_group": "未发现任何组（project-datas/ 下没有组目录）",
        "available": "可用组：",
        "choose": "请选择组编号: ",
        "choose_group": "已选择组: {name}（目录 {id}）",
        "ask_name": "请输入项目名（英文 ID）: ",
        "project_name": "项目名: {name}",
        "dup": "错误: 项目 '{name}' 已存在于组 {id} 中",
        "no_lang": "错误: project-meta/ 下没有任何语言文件，无法生成",
        "gen_langs": "将按 project-meta 基准语言生成: {langs}",
        "dir_exists": "错误: 目录已存在 {dir}",
        "created": "已创建项目条目：",
        "next": "下一步：",
        "step1": "  1. 编辑刚生成的 JSON，填入 url / intro / restores / license / authors",
        "step2": "  2. 运行 `python main.py generate` 重新生成 README",
        "step3": "  3. 运行 `python main.py lint` 校验数据",
        "bad_num": "请输入数字编号",
        "out_of_range": "编号超出范围（1-{count}）",
        "empty": "输入不能为空，请重试",
        "bad_name": "项目名只能含字母、数字、连字符、下划线，且不能以连字符/下划线开头",
        "cancel": "已取消",
    },
    "en-US": {
        "no_group": "No groups found (no group directories under project-datas/)",
        "available": "Available groups:",
        "choose": "Select a group number: ",
        "choose_group": "Selected group: {name} (directory {id})",
        "ask_name": "Enter a project name (English ID): ",
        "project_name": "Project name: {name}",
        "dup": "Error: project '{name}' already exists in group {id}",
        "no_lang": "Error: no language files under project-meta/, cannot generate",
        "gen_langs": "Will generate for project-meta base languages: {langs}",
        "dir_exists": "Error: directory already exists {dir}",
        "created": "Created project entry:",
        "next": "Next steps:",
        "step1": "  1. Edit the generated JSON to fill in url / intro / restores / license / authors",
        "step2": "  2. Run `python main.py generate` to regenerate the README",
        "step3": "  3. Run `python main.py lint` to validate the data",
        "bad_num": "Please enter a number",
        "out_of_range": "Number out of range (1-{count})",
        "empty": "Input cannot be empty, please retry",
        "bad_name": "Project name may only contain letters, digits, hyphens, underscores; cannot start with hyphen/underscore",
        "cancel": "Cancelled",
    },
}


def detect_ui_lang():
    """从系统 locale 检测界面语言，返回 'zh-CN' 或 'en-US'。"""
    # 1. 环境变量
    for var in ("LANG", "LC_ALL", "LC_MESSAGES"):
        val = os.environ.get(var, "")
        if val.lower().startswith("zh"):
            return "zh-CN"
        if val and not val.lower().startswith(("c", "posix")):
            return "en-US"
    # 2. locale 模块
    try:
        code = locale.getdefaultlocale()[0] or ""
        if code.lower().startswith("zh"):
            return "zh-CN"
    except Exception:
        pass
    return "en-US"


def _t(texts, key, **kw):
    return texts[key].format(**kw)


def _ask_choice(texts, prompt, count):
    while True:
        try:
            raw = input(prompt).strip()
        except (EOFError, KeyboardInterrupt):
            print(_t(texts, "cancel"))
            sys.exit(130)
        if raw == "":
            print(_t(texts, "empty"))
            continue
        try:
            idx = int(raw)
        except ValueError:
            print(_t(texts, "bad_num"))
            continue
        if 1 <= idx <= count:
            return idx - 1
        print(_t(texts, "out_of_range", count=count))


def _ask_project_name(texts, prompt):
    while True:
        try:
            raw = input(prompt).strip()
        except (EOFError, KeyboardInterrupt):
            print(_t(texts, "cancel"))
            sys.exit(130)
        if not PROJECT_NAME_RE.match(raw):
            print(_t(texts, "bad_name"))
            continue
        return raw


def _template(project_name, primary_lang, supported_langs):
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


def run(base, verbose=True, ui_lang=None):
    ui_lang = ui_lang or detect_ui_lang()
    texts = I18N.get(ui_lang, I18N["en-US"])
    collector = collect(base)

    # 1. 组列表
    groups = collector["groups"]
    if not groups:
        print(_t(texts, "no_group"))
        return 1

    print(_t(texts, "available"))
    group_names = []
    for i, g in enumerate(groups):
        gm = load_lang_file([
            os.path.join(g["meta_dir"], f"{ui_lang}.json"),
            os.path.join(g["meta_dir"], f"{FALLBACK_LANG}.json"),
        ])
        disp = gm["name"] if gm and "name" in gm else g["id"]
        group_names.append(disp)
        print(f"  {i + 1}. {disp}")

    gi = _ask_choice(texts, _t(texts, "choose"), len(groups))
    group = groups[gi]
    print(_t(texts, "choose_group", name=group_names[gi], id=group["id"]))

    # 2. 项目名
    project_name = _ask_project_name(texts, _t(texts, "ask_name"))
    print(_t(texts, "project_name", name=project_name))

    # 校验是否已存在同名项目
    for p in group["projects"]:
        if p["id"] == project_name:
            print(_t(texts, "dup", name=project_name, id=group["id"]))
            return 1

    # 3. 语言基准 = project-meta 文件名集合
    meta_langs = collector["meta"]["langs"]
    if not meta_langs:
        print(_t(texts, "no_lang"))
        return 1

    primary_lang = FALLBACK_LANG if FALLBACK_LANG in meta_langs else meta_langs[0]
    print(_t(texts, "gen_langs", langs=", ".join(meta_langs)))

    # 4. 创建文件夹 + 各语言 JSON
    proj_dir = os.path.join(group["dir"], project_name)
    if os.path.exists(proj_dir):
        print(_t(texts, "dir_exists", dir=proj_dir))
        return 1
    os.makedirs(proj_dir)

    created = []
    for lang in meta_langs:
        fpath = os.path.join(proj_dir, f"{lang}.json")
        data = _template(project_name, primary_lang, list(meta_langs))
        with open(fpath, "w", encoding="utf-8") as fh:
            json.dump(data, fh, ensure_ascii=False, indent=2)
            fh.write("\n")
        created.append(fpath)

    print(_t(texts, "created"))
    for fpath in created:
        print(f"  {fpath}")

    print(_t(texts, "next"))
    print(_t(texts, "step1"))
    print(_t(texts, "step2"))
    print(_t(texts, "step3"))
    return 0


def cmd(args):
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return run(base)
