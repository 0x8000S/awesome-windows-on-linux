# -*- coding: utf-8 -*-
"""generate — 生成 README。"""
import os

from core.config import DEFAULT_LANG, FALLBACK_LANG, GROUP_META_DIR
from core.render import render
from core.scanner import load_lang_file, lang_files_in


def run(base, lang, out_path=None):
    data_root = os.path.join(base, "project-datas")
    meta_root = os.path.join(base, "project-meta")

    # 所有可用语言（用于渲染语言切换链接）
    all_langs = lang_files_in(meta_root)

    meta = load_lang_file([
        os.path.join(meta_root, f"{lang}.json"),
        os.path.join(meta_root, f"{FALLBACK_LANG}.json"),
    ])
    if meta is None:
        raise SystemExit(
            f"未找到顶层元数据: project-meta/{lang}.json 或 {FALLBACK_LANG}.json")

    groups = []
    for groupid in os.listdir(data_root):
        group_dir = os.path.join(data_root, groupid)
        if not os.path.isdir(group_dir):
            continue
        gmeta = load_lang_file([
            os.path.join(group_dir, GROUP_META_DIR, f"{lang}.json"),
            os.path.join(group_dir, GROUP_META_DIR, f"{FALLBACK_LANG}.json"),
        ])
        if gmeta is None:
            continue

        projects = []
        for pid in os.listdir(group_dir):
            pdir = os.path.join(group_dir, pid)
            if pid == GROUP_META_DIR or not os.path.isdir(pdir):
                continue
            pdata = load_lang_file([
                os.path.join(pdir, f"{lang}.json"),
                os.path.join(pdir, f"{FALLBACK_LANG}.json"),
            ])
            if pdata is None:
                continue
            projects.append(pdata)

        groups.append({"meta": gmeta, "projects": projects})

    content = render(meta, groups, lang, all_langs)

    if out_path is None:
        out_path = os.path.join(
            base, "README.md" if lang == DEFAULT_LANG else f"README.{lang}.md")

    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(content)

    total = sum(len(g["projects"]) for g in groups)
    print(f"语言: {lang} | 已生成: {out_path}")
    print(f"共 {total} 个项目，{len(groups)} 个分组")
    return out_path


def cmd(args):
    base = os.path.dirname(os.path.abspath(__file__))
    base = os.path.dirname(base)  # 上一级为项目根
    return run(base, args.lang, args.out)
