# -*- coding: utf-8 -*-
"""cl — 检查语言不对称（check-language）。"""
from core.config import FALLBACK_LANG
from core.issues import IssueCollector
from core.scanner import load_lang_file


def run(collector, verbose=True):
    issues = IssueCollector()

    # 1. fallback 必须存在
    if FALLBACK_LANG not in collector["meta"]["langs"]:
        issues.add("error", "project-meta",
                   f"缺少 fallback 语言文件 {FALLBACK_LANG}.json")
    for g in collector["groups"]:
        if FALLBACK_LANG not in g["langs"]:
            issues.add("error", f"组 [{g['id']}]",
                       f"缺少 fallback 语言文件 {FALLBACK_LANG}.json")
        for p in g["projects"]:
            if FALLBACK_LANG not in p["langs"]:
                issues.add("error", f"项目 [{g['id']}/{p['id']}]",
                           f"缺少 fallback 语言文件 {FALLBACK_LANG}.json")

    # 2. 全库语言集合（所有实体的并集）
    all_langs = set(collector["meta"]["langs"])
    for g in collector["groups"]:
        all_langs |= set(g["langs"])
        for p in g["projects"]:
            all_langs |= set(p["langs"])

    # 3. 顶层 meta 语言应与全库语言并集对称
    meta_langs = set(collector["meta"]["langs"])
    missing_in_meta = all_langs - meta_langs
    extra_in_meta = meta_langs - all_langs
    if missing_in_meta:
        issues.add("error", "project-meta",
                   f"缺少语言文件（项目/组有但 meta 没有）: {sorted(missing_in_meta)}")
    if extra_in_meta:
        issues.add("warn", "project-meta",
                   f"多余语言文件（meta 有但项目/组没有）: {sorted(extra_in_meta)}")

    # 4. 组语言应与组内项目语言并集对称；组内项目之间也应对称
    for g in collector["groups"]:
        proj_langs = set()
        for p in g["projects"]:
            proj_langs |= set(p["langs"])
        g_langs = set(g["langs"])
        missing = proj_langs - g_langs
        extra = g_langs - proj_langs
        if missing:
            issues.add("error", f"组 [{g['id']}]",
                       f"组 metadata 缺少语言（项目有但组没有）: {sorted(missing)}")
        if extra:
            issues.add("warn", f"组 [{g['id']}]",
                       f"组 metadata 多余语言（组有但项目没有）: {sorted(extra)}")

        for p in g["projects"]:
            p_langs = set(p["langs"])
            missing = proj_langs - p_langs
            if missing:
                issues.add("error", f"项目 [{g['id']}/{p['id']}]",
                           f"缺少语言（组内其他项目有）: {sorted(missing)}")

    return issues


# 供 main 引用的入口
def cmd(collector):
    return run(collector)
