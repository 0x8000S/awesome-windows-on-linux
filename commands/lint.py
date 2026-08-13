# -*- coding: utf-8 -*-
"""lint — 综合检查（cl + check），适合 CI。"""
from core.issues import IssueCollector

from . import cl as cl_cmd
from . import check as check_cmd


def run(collector, verbose=True):
    issues = IssueCollector()
    for cmd in (cl_cmd, check_cmd):
        sub = cmd.run(collector, verbose)
        issues.items.extend(sub.items)
    return issues


def cmd(collector):
    return run(collector)
