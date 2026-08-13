# -*- coding: utf-8 -*-
"""Awesome Windows on Linux — 统一入口。

子命令:
    generate [--lang L] [--out F]   生成 README（默认命令）
    cl                              检查语言不对称（cl = check-language）
    check                           检查多定义 / 少定义（字段缺失、多余、重复 ID）
    lint                            综合检查（cl + check），适合 CI

目录结构:
    project-meta/{language}.json                      # 顶层元数据（标题、贡献、许可…）
    project-datas/{groupid}/awol-group-metadata/{language}.json   # 组的元数据
    project-datas/{groupid}/{ProjectID}/{language}.json           # 每个项目的信息
"""
import argparse
import os
import sys

# Windows 控制台默认 GBK，重配置 stdout 为 UTF-8 避免打印中文/符号报错
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

# 保证能以 python main.py 或 python main.py/目录 方式运行，兼容从任何 cwd
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from core.config import FALLBACK_LANG  # noqa: E402
from core.scanner import collect  # noqa: E402
from commands import cl, check, lint, generate  # noqa: E402


def _project_base():
    return os.path.dirname(os.path.abspath(__file__))


def main():
    parser = argparse.ArgumentParser(
        description="Awesome Windows on Linux — README 生成器 + 数据校验",
        prog="main.py")
    sub = parser.add_subparsers(dest="command")

    p_gen = sub.add_parser("generate", help="生成 README（默认命令）")
    p_gen.add_argument("--lang", default=FALLBACK_LANG, help="目标语言代码，默认 zh-CN")
    p_gen.add_argument("--out", default=None, help="输出文件路径")
    p_gen.set_defaults(func=lambda a: generate.run(_project_base(), a.lang, a.out))

    sub.add_parser("cl", help="检查语言不对称（cl = check-language）")
    sub.add_parser("check", help="检查多定义/少定义（字段缺失、多余、重复 ID）")
    sub.add_parser("lint", help="综合检查（cl + check），适合 CI")

    args = parser.parse_args()

    base = _project_base()

    if not args.command:
        # 默认命令 = generate
        generate.run(base, FALLBACK_LANG, None)
        return

    if args.command in ("cl", "check", "lint"):
        collector = collect(base)
        if args.command == "cl":
            issues = cl.run(collector)
        elif args.command == "check":
            issues = check.run(collector)
        else:
            issues = lint.run(collector)
        rc = issues.print(args.command)
        sys.exit(rc)
        return

    if args.command == "generate":
        args.func(args)
        return

    parser.print_help()


if __name__ == "__main__":
    main()
