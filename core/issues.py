# -*- coding: utf-8 -*-
"""issue 收集器与打印。"""


class IssueCollector:
    """收集校验问题。issue = (severity, scope, msg)，severity 为 'error' | 'warn'。"""

    def __init__(self):
        self.items = []

    def add(self, severity, scope, msg):
        self.items.append((severity, scope, msg))

    def errors(self):
        return [i for i in self.items if i[0] == "error"]

    def warnings(self):
        return [i for i in self.items if i[0] == "warn"]

    def print(self, name):
        if not self.items:
            print(f"[{name}] OK - 无问题")
            return 0
        errs = self.errors()
        warns = self.warnings()
        for sev, scope, msg in self.items:
            tag = "错误" if sev == "error" else "警告"
            print(f"[{name}] {tag}: {scope} — {msg}")
        print(f"[{name}] 共 {len(self.items)} 项（{len(errs)} 错误 / {len(warns)} 警告）")
        return 1 if errs else 0
