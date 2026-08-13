# -*- coding: utf-8 -*-
"""check — 检查多定义/少定义（字段缺失、多余字段、重复 ID）。"""
import os

from core.config import (FALLBACK_LANG, REQUIRED_FIELDS, KNOWN_EXTRA_FIELDS,
                         AUTHOR_FIELDS, INTENT_VALUES)
from core.issues import IssueCollector
from core.scanner import load_lang_file


def _check_unknown_fields(data, scope, kind, issues):
    """检查多余字段（多定义）：不在必需也不在已知额外集合内的字段。"""
    known = set(REQUIRED_FIELDS[kind]) | set(KNOWN_EXTRA_FIELDS.get(kind, []))
    for key in data:
        if key not in known:
            issues.add("warn", scope,
                       f"未识别的字段: '{key}'（若是有意新增请加入 KNOWN_EXTRA_FIELDS）")


def _check_authors(authors, scope, issues):
    """检查 authors 数组的结构。"""
    if not isinstance(authors, list):
        issues.add("error", scope, "authors 必须是数组")
        return
    for i, a in enumerate(authors):
        if not isinstance(a, dict):
            issues.add("error", scope, f"authors[{i}] 必须是对象")
            continue
        for f in AUTHOR_FIELDS:
            if f not in a or not str(a.get(f, "")).strip():
                issues.add("error", scope, f"authors[{i}] 缺少字段: {f}")


def _check_langs(pd, scope, issues):
    """检查 lang_primary / lang_supported。"""
    primary = pd.get("lang_primary")
    if not primary:
        issues.add("error", scope, "缺少 lang_primary")
    supported = pd.get("lang_supported")
    if not isinstance(supported, list) or not supported:
        issues.add("error", scope, "lang_supported 必须是非空数组")
    elif primary and primary not in supported:
        issues.add("warn", scope,
                   f"lang_primary '{primary}' 不在 lang_supported 中")


def _check_intent(pd, scope, issues):
    """检查 intent 标签是否合法（若存在）。"""
    intent = pd.get("intent")
    if intent is None:
        return
    if intent not in INTENT_VALUES:
        issues.add("error", scope,
                   f"intent 取值非法: '{intent}'（应为 {'/'.join(INTENT_VALUES)}）")


def run(collector, verbose=True):
    issues = IssueCollector()
    meta_dir = collector["meta"]["dir"]

    # 1. 必需字段缺失（少定义）
    meta = load_lang_file([os.path.join(meta_dir, f"{FALLBACK_LANG}.json")])
    if meta is not None:
        for f in REQUIRED_FIELDS["meta"]:
            if f not in meta:
                issues.add("error", "project-meta", f"缺少必需字段: {f}")
        _check_unknown_fields(meta, "project-meta", "meta", issues)

    seen_ids = {}
    for g in collector["groups"]:
        gm = load_lang_file([os.path.join(g["meta_dir"], f"{FALLBACK_LANG}.json")])
        if gm is not None:
            for f in REQUIRED_FIELDS["group"]:
                if f not in gm:
                    issues.add("error", f"组 [{g['id']}]", f"缺少必需字段: {f}")
            _check_unknown_fields(gm, f"组 [{g['id']}]", "group", issues)

        for p in g["projects"]:
            pd = load_lang_file([os.path.join(p["dir"], f"{FALLBACK_LANG}.json")])
            if pd is None:
                continue
            scope = f"项目 [{g['id']}/{p['id']}]"
            for f in REQUIRED_FIELDS["project"]:
                if f not in pd:
                    issues.add("error", scope, f"缺少必需字段: {f}")
            _check_unknown_fields(pd, scope, "project", issues)
            _check_authors(pd.get("authors"), scope, issues)
            _check_langs(pd, scope, issues)
            _check_intent(pd, scope, issues)

            # 重复 ID：用目录名作为 ID
            pid = p["id"]
            if pid in seen_ids and seen_ids[pid] != g["id"]:
                issues.add("error", scope,
                           f"ID '{pid}' 已在组 [{seen_ids[pid]}] 中定义过（重复定义）")
            else:
                seen_ids[pid] = g["id"]

            # 空值检查
            for f in ["url", "intro", "restores", "license"]:
                if f in pd and not str(pd[f]).strip():
                    issues.add("warn", scope, f"字段 '{f}' 为空")

    return issues


def cmd(collector):
    return run(collector)
