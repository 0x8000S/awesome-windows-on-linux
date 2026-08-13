# -*- coding: utf-8 -*-
"""根据 project-datas/ 与 project-meta/ 目录结构生成 README.md。

目录结构:
    project-meta/{language}.json                      # 顶层元数据（标题、贡献、许可…）
    project-datas/{groupid}/awol-group-metadata/{language}.json   # 组的元数据
    project-datas/{groupid}/{ProjectID}/{language}.json           # 每个项目的信息

用法:
    python generate_readme.py                 # 默认 zh-CN
    python generate_readme.py --lang en-US    # 生成英文版
    python generate_readme.py --lang en-US --out README.en.md

设计:
    - 数据按「语言目录」存放，天然支持多语言。
    - 某语言文件缺失时，回退到 fallback 语言（默认 zh-CN）。
    - 组内项目目录扫描自动发现，新增项目只需新建文件夹。
"""
import argparse
import json
import os


# 固定的元数据目录名
GROUP_META_DIR = "awol-group-metadata"
FALLBACK_LANG = "zh-CN"


def load_json(path):
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)


def load_lang_file(path_candidates):
    """按优先级返回第一个存在的 JSON；全缺返回 None。"""
    for p in path_candidates:
        if os.path.exists(p):
            return load_json(p)
    return None


def load_group_meta(group_dir, lang, fallback):
    """读取组元数据，优先 lang，回退 fallback。"""
    base = os.path.join(group_dir, GROUP_META_DIR)
    return load_lang_file([
        os.path.join(base, f"{lang}.json"),
        os.path.join(base, f"{fallback}.json"),
    ])


def load_project(project_dir, lang, fallback):
    return load_lang_file([
        os.path.join(project_dir, f"{lang}.json"),
        os.path.join(project_dir, f"{fallback}.json"),
    ])


def discover(data_root, lang, fallback):
    """扫描目录树，返回 (meta, groups)。"""
    meta_root = os.path.join(os.path.dirname(data_root), "project-meta")
    meta = load_lang_file([
        os.path.join(meta_root, f"{lang}.json"),
        os.path.join(meta_root, f"{fallback}.json"),
    ])
    if meta is None:
        raise SystemExit(f"未找到顶层元数据: project-meta/{lang}.json 或 {fallback}.json")

    groups = []
    # 展示顺序 = 目录在磁盘上的顺序，不额外排序，由目录结构本身决定
    for groupid in os.listdir(data_root):
        group_dir = os.path.join(data_root, groupid)
        if not os.path.isdir(group_dir):
            continue
        gmeta = load_group_meta(group_dir, lang, fallback)
        if gmeta is None:
            continue

        projects = []
        # 每个子目录（除 awol-group-metadata 外）是一个项目
        for pid in os.listdir(group_dir):
            pdir = os.path.join(group_dir, pid)
            if pid == GROUP_META_DIR or not os.path.isdir(pdir):
                continue
            pdata = load_project(pdir, lang, fallback)
            if pdata is None:
                continue
            projects.append(pdata)

        groups.append({"meta": gmeta, "projects": projects})

    return meta, groups


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
    f_author = fields.get("author", "作者")
    f_lang = fields.get("lang", "语言")
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
            lines.append(f"- {f_author}：[{p['author']}]({p['author_url']})")
            lines.append(f"- {f_lang}：" + p["lang"])
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


def main():
    parser = argparse.ArgumentParser(description="生成 Awesome Windows on Linux README")
    parser.add_argument("--lang", default=FALLBACK_LANG, help="目标语言代码，默认 zh-CN")
    parser.add_argument("--out", default=None, help="输出文件路径，默认 README.<lang>.md 或 README.md")
    args = parser.parse_args()

    base = os.path.dirname(os.path.abspath(__file__))
    data_root = os.path.join(base, "project-datas")

    meta, groups = discover(data_root, args.lang, FALLBACK_LANG)
    content = render(meta, groups)

    if args.out:
        out_path = args.out
    else:
        out_path = os.path.join(base,
            "README.md" if args.lang == FALLBACK_LANG else f"README.{args.lang}.md")

    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(content)

    total = sum(len(g["projects"]) for g in groups)
    print(f"语言: {args.lang} | 已生成: {out_path}")
    print(f"共 {total} 个项目，{len(groups)} 个分组")


if __name__ == "__main__":
    main()
