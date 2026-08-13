# -*- coding: utf-8 -*-
"""目录树扫描：把 project-datas / project-meta 结构收集成内存中的实体集合。"""
import os

from .config import GROUP_META_DIR


def load_json(path):
    import json
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)


def load_lang_file(path_candidates):
    """按优先级返回第一个存在的 JSON；全缺返回 None。"""
    for p in path_candidates:
        if os.path.exists(p):
            return load_json(p)
    return None


def lang_files_in(dirpath):
    """返回目录下所有 json 的语言代码列表（去掉扩展名），确定性排序。"""
    if not os.path.isdir(dirpath):
        return []
    return sorted(f[:-5] for f in os.listdir(dirpath) if f.endswith(".json"))


def collect(base):
    """扫描整个目录树，返回结构化的实体集合。

    返回:
        {
          "base": ...,
          "meta": {"dir": ..., "langs": [...]},
          "groups": [ {"id":..., "dir":..., "langs":[...], "meta_dir":...,
                       "projects":[ {"id":..., "dir":..., "langs":[...]} ]} ]
        }
    """
    data_root = os.path.join(base, "project-datas")
    meta_root = os.path.join(base, "project-meta")

    result = {
        "base": base,
        "meta": {"dir": meta_root, "langs": lang_files_in(meta_root)},
        "groups": [],
    }

    if not os.path.isdir(data_root):
        return result

    for groupid in sorted(os.listdir(data_root)):
        group_dir = os.path.join(data_root, groupid)
        if not os.path.isdir(group_dir):
            continue
        meta_dir = os.path.join(group_dir, GROUP_META_DIR)
        group = {
            "id": groupid,
            "dir": group_dir,
            "langs": lang_files_in(meta_dir),
            "meta_dir": meta_dir,
            "projects": [],
        }
        for pid in sorted(os.listdir(group_dir)):
            pdir = os.path.join(group_dir, pid)
            if pid == GROUP_META_DIR or not os.path.isdir(pdir):
                continue
            group["projects"].append({
                "id": pid,
                "dir": pdir,
                "langs": lang_files_in(pdir),
            })
        result["groups"].append(group)

    return result
