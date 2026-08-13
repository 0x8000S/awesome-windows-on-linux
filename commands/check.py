# -*- coding: utf-8 -*-
"""check — 检查多定义/少定义（字段缺失、多余字段、重复 ID）。"""
import os

from core.config import FALLBACK_LANG, REQUIRED_FIELDS, KNOWN_EXTRA_FIELDS
from core.issues import IssueCollector
from core.scanner import load_lang_file


def _check_unknown_fields(data, scope, kind, issues):
    """检查多余字段（多定义）：不在必需也不在已知额外集合内的字段。"""
    known = set(REQUIRED_FIELDS[kind]) | set(KNOWN_EXTRA_FIELDS.get(kind, []))
    for key in data:
        if key not in known:
            issues.add("warn", scope,
                       f"未识别的字段: '{key}'（若是有意新增请加入 KNOWN_EXTRA_FIELDS）")


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
            for f in REQUIRED_FIELDS["project"]:
                if f not in pd:
                    issues.add("error", f"项目 [{g['id']}/{p['id']}]",
                               f"缺少必需字段: {f}")
            _check_unknown_fields(pd, f"项目 [{g['id']}/{p['id']}]", "project", issues)

            # 重复 ID：同一 id 出现在不同组
            pid = pd.get("id") or p["id"]
            if pid in seen_ids and seen_ids[pid] != g["id"]:
                issues.add("error", f"项目 [{g['id']}/{p['id']}]",
                           f"ID '{pid}' 已在组 [{seen_ids[pid]}] 中定义过（重复定义）")
            else:
                seen_ids[pid] = g["id"]

            # 空值检查
            for f in ["url", "intro", "restores", "license", "author", "author_url"]:
                if f in pd and not str(pd[f]).strip():
                    issues.add("warn", f"项目 [{g['id']}/{p['id']}]",
                               f"字段 '{f}' 为空")

    return issues


def cmd(collector):
    return run(collector)
