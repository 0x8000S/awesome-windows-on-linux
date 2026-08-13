# -*- coding: utf-8 -*-
"""全局常量与字段白名单配置。"""

# 固定的元数据目录名
GROUP_META_DIR = "awol-group-metadata"
FALLBACK_LANG = "zh-CN"

# 各实体的必需字段（少定义检查基准）
REQUIRED_FIELDS = {
    "meta": ["title", "tagline", "description", "notice", "toc_title",
             "contribute_title", "contribute_text", "license_title",
             "license", "license_link", "year", "owner"],
    "group": ["name", "note"],
    "project": ["name", "url", "intro", "restores", "license",
                "authors", "lang_primary", "lang_supported"],
}

# 各实体可含的额外字段（多定义检查时警告，但不算错误）
KNOWN_EXTRA_FIELDS = {
    "meta": ["fields"],
    "group": ["id"],
    "project": ["video"],
}

# 作者数组的元素结构
AUTHOR_FIELDS = ["name", "url"]
