# -*- coding: utf-8 -*-
"""把 meta + groups 渲染为 README markdown 文本。"""


def slugify(name):
    """把分组名转成 markdown 锚点（小写、空格/斜杠/点替换为 '-'）。"""
    s = name.strip().lower()
    for ch in [" ", "/", ".", "_", "（", "）", "(", ")"]:
        s = s.replace(ch, "-")
    s = s.replace("--", "-")
    return s


def render(meta, groups):
    fields = meta.get("fields", {})
    f_intro = fields.get("intro", "介绍")
    f_restores = fields.get("restores", "还原的部分")
    f_license = fields.get("license", "许可证")
    f_authors = fields.get("authors", "作者")
    f_lang_primary = fields.get("lang_primary", "主要语言")
    f_lang_supported = fields.get("lang_supported", "支持语言")
    f_video = fields.get("video", "介绍视频")
    f_video_pending = fields.get("video_pending", "（待补充）")

    lines = []
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
    lines.append(f"## {meta.get('toc_title', '目录')}")
    lines.append("")
    for g in groups:
        lines.append(f"- [{g['meta']['name']}](#{slugify(g['meta']['name'])})")
    lines.append("")
    lines.append("---")
    lines.append("")

    # 分组 + 项目
    for g in groups:
        gm = g["meta"]
        lines.append(f"## {gm['name']}")
        lines.append("")
        lines.append(f"> {gm['note']}")
        lines.append("")
        for p in g["projects"]:
            lines.append(f"### [{p['name']}]({p['url']})")
            lines.append("")
            lines.append(f"{f_intro}：{p['intro']}")
            lines.append("")
            lines.append(f"{f_restores}：{p['restores']}")
            lines.append("")
            lines.append(f"- {f_license}：" + p["license"])
            # 作者数组
            authors = p.get("authors", [])
            author_links = [f"[{a['name']}]({a['url']})" for a in authors]
            lines.append(f"- {f_authors}：" + "、".join(author_links))
            # 语言
            lines.append(f"- {f_lang_primary}：" + p.get("lang_primary", ""))
            supported = p.get("lang_supported", [])
            lines.append(f"- {f_lang_supported}：" + " / ".join(supported))
            video = p.get("video", "")
            lines.append(f"- {f_video}：{video if video else f_video_pending}")
            lines.append("")

    # 贡献 / 许可
    lines.append("---")
    lines.append("")
    lines.append(f"## {meta.get('contribute_title', '贡献')}")
    lines.append("")
    lines.append(meta.get("contribute_text", ""))
    lines.append("")
    lines.append(f"## {meta.get('license_title', '许可')}")
    lines.append("")
    lines.append(f"[{meta['license']}]({meta['license_link']}) "
                 f"© {meta['year']} {meta['owner']}")
    lines.append("")

    return "\n".join(lines)
