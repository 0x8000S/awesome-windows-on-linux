# -*- coding: utf-8 -*-
"""根据 projects.json 生成 README.md。

用法:
    python generate_readme.py                 # 使用默认路径 projects.json / README.md
    python generate_readme.py data.json out.md

设计:
    - 数据全部存放在 projects.json，本脚本只负责排版。
    - 新增 / 修改项目只需编辑 JSON，然后重跑本脚本。
"""
import json
import os
import sys


def load_json(path):
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)


def render(data):
    meta = data["meta"]
    groups = data["groups"]

    lines = []

    # 标题
    lines.append(f"# {meta['title']}")
    lines.append("")
    lines.append(f"> {meta['tagline']}")
    lines.append("")
    lines.append("[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)")
    lines.append(f"[![License: {meta['license']}]"
                 f"(https://img.shields.io/badge/License-{meta['license']}-blue.svg)]"
                 f"({meta['license_link']})")
    lines.append("")
    lines.append(meta["description"])
    lines.append("")
    lines.append(f"> **阅读说明**：{meta['notice']}")
    lines.append("")
    lines.append("---")
    lines.append("")

    # 目录
    lines.append("## 目录")
    lines.append("")
    for g in groups:
        lines.append(f"- [{g['name']}](#{g['anchor']})")
    lines.append("")
    lines.append("---")
    lines.append("")

    # 分组 + 项目
    for g in groups:
        lines.append(f"## {g['name']}")
        lines.append("")
        lines.append(f"> {g['note']}")
        lines.append("")
        for p in g["projects"]:
            lines.append(f"### [{p['name']}]({p['url']})")
            lines.append("")
            lines.append(f"介绍：{p['intro']}")
            lines.append("")
            lines.append(f"还原的部分：{p['restores']}")
            lines.append("")
            lines.append("- 许可证：" + p["license"])
            lines.append(f"- 作者：[{p['author']}]({p['author_url']})")
            lines.append("- 语言：" + p["lang"])
            video = p.get("video", "")
            lines.append(f"- 介绍视频：{video if video else '（待补充）'}")
            lines.append("")

    # 贡献 / 许可
    lines.append("---")
    lines.append("")
    lines.append("## 贡献")
    lines.append("")
    lines.append("欢迎提交 PR 补充更多「Windows on Linux」项目。"
                 "条目建议包含：项目链接、许可证、作者、主要 / 支持语言、"
                 "一句话介绍、还原的部分。")
    lines.append("")
    lines.append("## 许可")
    lines.append("")
    lines.append(f"[{meta['license']}]({meta['license_link']}) "
                 f"© {meta['year']} {meta['owner']}")
    lines.append("")

    return "\n".join(lines)


def main():
    json_path = sys.argv[1] if len(sys.argv) > 1 else "projects.json"
    out_path = sys.argv[2] if len(sys.argv) > 2 else "README.md"

    # 脚本所在目录作为基准，兼容从任意 cwd 运行
    base = os.path.dirname(os.path.abspath(__file__))
    json_path = json_path if os.path.isabs(json_path) else os.path.join(base, json_path)
    out_path = out_path if os.path.isabs(out_path) else os.path.join(base, out_path)

    data = load_json(json_path)
    content = render(data)
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(content)

    print(f"已生成: {out_path}")
    print(f"共 {sum(len(g['projects']) for g in data['groups'])} 个项目"
          f"，{len(data['groups'])} 个分组")


if __name__ == "__main__":
    main()
