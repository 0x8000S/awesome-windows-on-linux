# -*- coding: utf-8 -*-
"""cl — 检查语言不对称（check-language）。

判断基准：project-meta/ 下的文件名集合（meta_langs）。
所有组、项目的支持语言（各自目录下的 .json 文件名）必须与该基准完全一致，
多一个（多余语言）或少一个（缺少语言）都报错。

即：project-meta 是全库唯一语言基准，其余实体必须对齐。
"""
from core.config import FALLBACK_LANG
from core.issues import IssueCollector


def run(collector, verbose=True):
    issues = IssueCollector()

    # 基准：project-meta/ 下的语言文件名
    meta_langs = set(collector["meta"]["langs"])
    _ = verbose

    # 1. fallback 语言必须在基准内（project-meta 必须有 fallback 文件）
    if FALLBACK_LANG not in meta_langs:
        issues.add("error", "project-meta",
                   f"缺少 fallback 语言文件 {FALLBACK_LANG}.json")

    # 2. 每个组的语言必须与基准完全一致
    for g in collector["groups"]:
        g_langs = set(g["langs"])
        missing = meta_langs - g_langs
        extra = g_langs - meta_langs
        if missing:
            issues.add("error", f"组 [{g['id']}]",
                       f"缺少语言（与 project-meta 基准对齐）: {sorted(missing)}")
        if extra:
            issues.add("error", f"组 [{g['id']}]",
                       f"多余语言（与 project-meta 基准对齐）: {sorted(extra)}")

        # 3. 组内每个项目的语言也必须与基准完全一致
        for p in g["projects"]:
            p_langs = set(p["langs"])
            missing = meta_langs - p_langs
            extra = p_langs - meta_langs
            if missing:
                issues.add("error", f"项目 [{g['id']}/{p['id']}]",
                           f"缺少语言（与 project-meta 基准对齐）: {sorted(missing)}")
            if extra:
                issues.add("error", f"项目 [{g['id']}/{p['id']}]",
                           f"多余语言（与 project-meta 基准对齐）: {sorted(extra)}")

    return issues


# 供 main 引用的入口
def cmd(collector):
    return run(collector)
