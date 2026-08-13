# -*- coding: utf-8 -*-
"""把 meta + groups 渲染为 README markdown 文本。"""
from .config import DEFAULT_LANG


def _language_switcher(current_lang, all_langs):
    """生成语言切换链接行。

    - 默认语言（DEFAULT_LANG）链接到 README.md
    - 其他语言链接到 README.<lang>.md
    - 当前语言加粗标记
    返回空字符串表示无需切换（只有一种语言）。
    """
    if not all_langs or len(all_langs) < 2:
        return ""
    parts = []
    for lang in all_langs:
        label = lang
        if lang == DEFAULT_LANG:
            href = "README.md"
        else:
            href = f"README.{lang}.md"
        if lang == current_lang:
            parts.append(f"**{label}**")
        else:
            parts.append(f"[{label}]({href})")
    return " | ".join(parts)


def slugify(name):
    """把分组名转成 markdown 锚点（小写、空格/斜杠/点替换为 '-'）。"""
    s = name.strip().lower()
    for ch in [" ", "/", ".", "_", "（", "）", "(", ")"]:
        s = s.replace(ch, "-")
    s = s.replace("--", "-")
    return s


def render(meta, groups, lang, all_langs, generated_at=""):
    fields = meta.get("fields", {})
    f_intro = fields.get("intro", "介绍")
    f_restores = fields.get("restores", "还原的部分")
    f_license = fields.get("license", "许可证")
    f_authors = fields.get("authors", "作者")
    f_lang_primary = fields.get("lang_primary", "主要语言")
    f_lang_supported = fields.get("lang_supported", "支持语言")
    f_video = fields.get("video", "介绍视频")
    f_video_pending = fields.get("video_pending", "（待补充）")
    f_generated_at = fields.get("generated_at", "Generated at")

    # 冒号：中文用全角，其他语言用半角
    colon = "：" if lang.startswith("zh") else ": "

    lines = []
    lines.append(f"# {meta['title']}")
    lines.append("")
    lines.append(f"> {meta['tagline']}")
    lines.append("")

    # 语言切换链接（README.md 默认 + README.<lang>.md 其他）
    switcher = _language_switcher(lang, all_langs)
    if switcher:
        lines.append(switcher)
        lines.append("")

    lines.append("[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)")
    lines.append(f"[![License: {meta['license']}]"
                 f"(https://img.shields.io/badge/License-{meta['license']}-blue.svg)]"
                 f"({meta['license_link']})")
    lines.append("")
    lines.append(meta["description"])
    lines.append("")
    # 阅读说明可选：有值才输出
    if meta.get("notice"):
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
            lines.append(f"{f_intro}{colon}{p['intro']}")
            lines.append("")
            lines.append(f"{f_restores}{colon}{p['restores']}")
            lines.append("")
            lines.append(f"- {f_license}{colon}" + p["license"])
            # 作者数组
            authors = p.get("authors", [])
            author_links = [f"[{a['name']}]({a['url']})" for a in authors]
            lines.append(f"- {f_authors}{colon}" + "、".join(author_links))
            # 语言
            lines.append(f"- {f_lang_primary}{colon}" + p.get("lang_primary", ""))
            supported = p.get("lang_supported", [])
            lines.append(f"- {f_lang_supported}{colon}" + " / ".join(supported))
            video = p.get("video", "")
            lines.append(f"- {f_video}{colon}{video if video else f_video_pending}")
            lines.append("")

    # 贡献
    lines.append("---")
    lines.append("")
    lines.append(f"## {meta.get('contribute_title', '贡献')}")
    lines.append("")
    lines.append(meta.get("contribute_text", ""))
    lines.append("")

    # 教程（创建自己的项目条目）
    guide_title = meta.get("guide_title", "")
    guide = meta.get("guide", [])
    if guide_title and guide:
        lines.append(f"### {guide_title}")
        lines.append("")
        lines.extend(guide)
        lines.append("")

    # 许可
    lines.append("---")
    lines.append("")
    lines.append(f"## {meta.get('license_title', '许可')}")
    lines.append("")
    lines.append(f"[{meta['license']}]({meta['license_link']}) "
                 f"© {meta['year']} {meta['owner']}")
    lines.append("")

    # 生成时间戳（可复现性：每次生成都不同，便于每日构建产生提交）
    if generated_at:
        lines.append("")
        lines.append(f"*{f_generated_at}: {generated_at}*")
        lines.append("")

    return "\n".join(lines)
