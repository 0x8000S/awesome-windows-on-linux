# Awesome Windows on Linux (Only funny)

> 把 Windows 的「体验」搬到 Linux 上的项目合集 —— 从硬核逆向到恶趣味整活，一网打尽。

[en-US](README.md) | **zh-CN**

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

这个列表收录了在 Linux 上复刻 / 模拟 / 恶搞 Windows 生态的开源项目。按「整活浓度」从高到低排列，分为**硬核逆向**、**实用工具**、**GUI 复刻**、**整活恶搞**四大类。

---

## 目录

- [实用工具](#实用工具)
- [硬核逆向 / 底层格式](#硬核逆向--底层格式)
- [GUI 复刻](#gui-复刻)
- [整活恶搞](#整活恶搞)

---

## 实用工具

> 能把 Windows 工具链带到 Linux 的「瑞士军刀」。

### [aptx](https://github.com/WenAnrong/aptx)

介绍：apt 的增强封装，装 / 卸软件后自动推荐同类软件。

还原的部分：装软件时的「全家桶推荐」流氓体验。

- 许可证：MIT
- 作者：[WenAnrong](https://github.com/WenAnrong)
- 主要语言：en-US
- 支持语言：en-US / zh-CN
- 介绍视频：（待补充）

### [cmd](https://github.com/ChenPi11/cmd)

介绍：从零用纯 C89 忠实重写 Windows `cmd.exe` 的命令解释器，纯 POSIX 零依赖，能跑在任何 Unix 上。

还原的部分：Windows `cmd.exe` 命令行解释器（批处理、管道重定向、40+ 内置命令）。

- 许可证：GPL-3.0
- 作者：[ChenPi11](https://github.com/ChenPi11)
- 主要语言：en-US
- 支持语言：en-US / zh-CN / zh-MS / zh-WY
- 介绍视频：（待补充）

### [runbox](https://github.com/HelloAIXIAOJI/runbox)

介绍：Linux 上按下 `Super+R` 弹出的运行对话框，Adwaita 外观随系统主题。

还原的部分：Win+R「运行」对话框。

- 许可证：MIT
- 作者：[HelloAIXIAOJI](https://github.com/HelloAIXIAOJI)
- 主要语言：en-US
- 支持语言：en-US / zh-CN
- 介绍视频：（待补充）

### [Windowshit](https://github.com/HelloAIXIAOJI/windowshit)

介绍：用 Rust 重写的 Windows 命令行工具合集，跨平台运行。

还原的部分：24 个 Windows 命令行工具（ipconfig / ping / robocopy / systeminfo…）。

- 许可证：MIT
- 作者：[HelloAIXIAOJI](https://github.com/HelloAIXIAOJI)
- 主要语言：en-US
- 支持语言：en-US / zh-CN
- 介绍视频：（待补充）

## 硬核逆向 / 底层格式

> 正经技术项目：研究 Windows 程序怎么在 Linux 上存活。

### [LinuxForWindows](https://github.com/dyz131005/LinuxForWindows)

介绍：从文件格式层面把 Windows PE 可执行文件离线转换为 Linux ELF 的二进制转换工具。

还原的部分：PE / ELF 文件格式结构（头、节表、程序头、动态段）。

- 许可证：MIT
- 作者：[dyz131005](https://github.com/dyz131005)
- 主要语言：zh-CN
- 支持语言：zh-CN
- 介绍视频：（待补充）

## GUI 复刻

> 复刻 Windows 桌面 GUI 体验。

### [Explorer-for-Linux](https://github.com/macOS-Terminal/Explorer-for-Linux)

介绍：在 Linux 上深度复刻 Win11 文件管理体验的桌面程序。

还原的部分：Win11 资源管理器界面（含经典「未响应」体验）。

- 许可证：未标注
- 作者：[macOS-Terminal](https://github.com/macOS-Terminal)
- 主要语言：zh-CN
- 支持语言：zh-CN
- 介绍视频：（待补充）

### [mmclinux](https://gitee.com/windowsuninstaller/mmclinux)

介绍：仿 Windows 管理控制台的跨平台工具，基于 tkinter 实现。

还原的部分：MMC 管理控制台（MDI 子窗口、管理单元、窗口嵌套）。

- 许可证：MIT
- 作者：[WindowsUninstaller](https://gitee.com/windowsuninstaller)
- 主要语言：zh-CN
- 支持语言：zh-CN / en-US
- 介绍视频：（待补充）

### [regedit](https://github.com/heyManNice/regedit)

介绍：把 `/etc`、`~/.config`、`/boot` 映射成注册表树、自动嗅探多种配置格式的系统配置文件浏览器。

还原的部分：注册表编辑器界面（左侧树 + 右侧键值）。

- 许可证：GPL-3.0（README 声明，未附 LICENSE 文件）
- 作者：[heyManNice](https://github.com/heyManNice)
- 主要语言：zh-CN
- 支持语言：zh-CN
- 介绍视频：（待补充）

## 整活恶搞

> 纯整活，别在生产机器上乱跑。

### [adpop](https://github.com/MEKCCK/adpop)

介绍：完全自绘渲染、供其他软件调用的通用广告弹窗服务。

还原的部分：仿 Windows 流氓广告弹窗（动图 / 视频 / 音频 / 弹窗轰炸 / 流氓关闭）。

- 许可证：未标注
- 作者：[MEKCCK](https://github.com/MEKCCK)
- 主要语言：zh-CN
- 支持语言：zh-CN
- 介绍视频：（待补充）

### [bsod](https://github.com/heyManNice/bsod)

介绍：在 Linux 物理屏上直接渲染、抢占 DRM Master 的蓝屏演示工具，支持多语言与日志监控。

还原的部分：Win10 蓝屏死机界面（含二维码）。

- 许可证：MIT
- 作者：[heyManNice](https://github.com/heyManNice)
- 主要语言：en-US
- 支持语言：en-US / zh-CN / zh-TW / ja / ko
- 介绍视频：（待补充）

### [windows_update_in_linux](https://github.com/WenAnrong/windows_update_in_linux)

介绍：伪 Windows 更新界面的整活程序，每次运行 50% 真更新重启、50% 蓝屏。

还原的部分：Windows 更新界面（成功进度 / 失败蓝屏）。

- 许可证：MIT
- 作者：[WenAnrong](https://github.com/WenAnrong)
- 主要语言：en-US
- 支持语言：en-US / zh-CN
- 介绍视频：（待补充）

---

## 贡献

欢迎提交 PR 补充更多「Windows on Linux」项目。条目建议包含：项目链接、许可证、作者、主要 / 支持语言、一句话介绍、还原的部分。

### 创建自己的项目条目

想收录你的项目？最简单的方式是用交互式命令自动生成条目骨架，再补全信息。

### 一、交互式创建

运行：

```bash
python main.py new
```

按提示依次完成：

1. **选择组**：从列表输入组编号（例如输入 `1` 选择「实用工具」）。
2. **输入项目名**：填写英文 ID，仅允许字母、数字、连字符 `-`、下划线 `_`，且不能以连字符/下划线开头（例如 `my-awesome-tool`）。
3. **自动生成**：脚本会在 `project-datas/<组ID>/<项目名>/` 下，按 `project-meta/` 的语言基准为每种语言生成一个 JSON 文件。

### 二、生成的目录结构

```text
project-datas/
├── 1utilities/                  # 组目录（数字前缀控制展示顺序）
│   ├── awol-group-metadata/     # 组的元数据（名称、说明）
│   │   ├── zh-CN.json
│   │   └── en-US.json
│   └── my-awesome-tool/         # 你的项目目录
│       ├── zh-CN.json
│       └── en-US.json
└── ...
```

### 三、填写字段

打开生成的项目 JSON（如 `my-awesome-tool/zh-CN.json`），它初始如下：

```json
{
  "name": "my-awesome-tool",
  "intro": "",
  "restores": "",
  "license": "",
  "video": "",
  "url": "",
  "authors": [],
  "lang_primary": "zh-CN",
  "lang_supported": ["zh-CN"]
}
```

| 字段 | 必填 | 说明 |
| --- | --- | --- |
| `name` | ✅ | 项目显示名 |
| `url` | ✅ | 项目仓库地址 |
| `intro` | ✅ | 一句话介绍（这个项目是做什么的） |
| `restores` | ✅ | 还原了 Windows 的哪个部分（与 `intro` 分开） |
| `license` | ✅ | 开源许可证（如 `MIT`、`GPL-3.0`） |
| `authors` | ✅ | 作者数组，每项含 `name`（GitHub 用户名）与 `url` |
| `lang_primary` | ✅ | 主要语言（维护者最常用的） |
| `lang_supported` | ✅ | 支持的语言数组 |
| `video` | ⬜ | 介绍视频链接（可留空，显示「待补充」） |

> 提示：`intro` 讲「项目本身是什么」，`restores` 讲「复刻了 Windows 的哪部分」，两者不要混写。

### 四、重新生成与校验

编辑完成后，重新生成 README 并运行校验：

```bash
python main.py generate --lang zh-CN   # 重新生成中文 README
python main.py generate --lang en-US   # 重新生成英文 README
python main.py lint                    # 综合校验（lint = cl + check）
python main.py check                   # 只查字段多定义/少定义
python main.py cl                      # 只查语言不对称
```

确保 `lint` 输出 `OK - 无问题` 后再提交。

### 五、提交与 PR

```bash
git add .
git commit -m "feat: add my-awesome-tool"
git push
```

然后创建 Pull Request。CI 会在 PR 上自动运行 `lint`（含 `check`、`cl`）和「可复现性检查」，全部通过才能合并。

### 常见问题

- **`lint` 报错**：通常是因为字段缺失或语言不对称。运行 `python main.py check` 和 `python main.py cl` 定位具体问题。
- **语言不对称**：如果 `project-meta/` 里有 `en-US`，那么每个项目都要有 `en-US.json` 和 `zh-CN.json`，不能只填一种。
- **想删除条目**：删掉 `project-datas/<组ID>/<项目名>/` 整个目录，再重新 `generate` 即可。

---

## 许可

[MIT](LICENSE) © 2026 windowix


*生成于: 2026-08-13 14:00 UTC*
