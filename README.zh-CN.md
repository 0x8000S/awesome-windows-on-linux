# Awesome Windows on Linux (Only funny)

<p align="center"><img src="awologo.png" alt="Awesome Windows on Linux Logo" width="520"></p>

> 把 Windows 的「体验」搬到 Linux 上的项目合集 —— 从硬核逆向到恶趣味整活，一网打尽。

[en-US](README.md) | **zh-CN**

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

这个列表收录了在 Linux 上复刻 / 模拟 / 恶搞 Windows 生态的开源项目。项目按**形态**分组（命令行工具、GUI 应用、系统交互、底层 / 逆向），并给每个项目打了**意图标签**——`[实用]` 表示真能日常用，`[整活]` 表示恶搞、别在生产机跑。

---

## 目录

- [信息](#信息)
- [命令行工具](#命令行工具)
- [GUI 应用](#gui-应用)
- [系统交互](#系统交互)
- [底层 / 逆向](#底层--逆向)

- **文档**
  - [贡献](#贡献)
  - [创建自己的项目条目](#创建自己的项目条目)
  - [常见问题](#常见问题)
  - [许可](#许可)

---

## 信息

> 我也不知道该在这里放啥，哈哈哈。

### [Awesome Windows on Linux](https://github.com/windowix/awesome-windows-on-linux)

介绍：收录并整理在 Linux 上复刻 / 模拟 / 恶搞 Windows 生态的开源项目合集。

还原的部分：收录与整理还原Windows的项目

- 许可证：MIT
- 作者：[windowix](https://github.com/windowix)、[HelloAIXIAOJI](https://github.com/HelloAIXIAOJI)
- 主要语言：en-US
- 支持语言：en-US / zh-CN
- 介绍视频：https://www.bilibili.com/video/BV1mMgs6gET6

## 命令行工具

> 在 Unix 上还原 Windows 终端命令的命令行工具。

### [aptx](https://github.com/WenAnrong/aptx)

介绍：apt 的增强封装，装 / 卸软件后自动推荐同类软件。

还原的部分：装软件时的「全家桶推荐」流氓体验。

- 许可证：MIT
- 作者：[WenAnrong](https://github.com/WenAnrong)
- 主要语言：zh-CN
- 支持语言：en-US / zh-CN
- 介绍视频：https://www.bilibili.com/video/BV1LNgG69EMe

### [cmd](https://github.com/ChenPi11/cmd) [实用]

介绍：从零用纯 C89 忠实重写 Windows `cmd.exe` 的命令解释器，纯 POSIX 零依赖，能跑在任何 Unix 上。

还原的部分：Windows `cmd.exe` 命令行解释器（批处理、管道重定向、40+ 内置命令）。

- 许可证：GPL-3.0
- 作者：[ChenPi11](https://github.com/ChenPi11)
- 主要语言：en-US
- 支持语言：en-US / zh-CN / zh-MS / zh-WY
- 介绍视频：https://www.bilibili.com/video/BV1wkuH64EE8

### [Windowshit](https://github.com/HelloAIXIAOJI/windowshit) [实用]

介绍：用 Rust 重写的 Windows 命令行工具合集，跨平台运行。

还原的部分：24 个 Windows 命令行工具（ipconfig / ping / robocopy / systeminfo…）。

- 许可证：MIT
- 作者：[HelloAIXIAOJI](https://github.com/HelloAIXIAOJI)
- 主要语言：zh-CN
- 支持语言：en-US / zh-CN
- 介绍视频：https://www.bilibili.com/video/BV1Pzuy6oEZm

## GUI 应用

> 复刻 Windows 桌面界面的图形应用程序。

### [Lindows_Control](https://github.com/BobbyChengCN0518/Lindows_Control) [整活]

介绍：我修复了Linux上不能使用控制面板的Bug 
 可以通过json文件配置改语言，默认支持zh和en两种语言

还原的部分：控制面板

- 许可证：MIT
- 作者：[BobbyChengCN0518](https://github.com/BobbyChengCN0518)
- 主要语言：zh-CN
- 支持语言：zh-CN / en-US
- 介绍视频：（待补充）

### [WinSAT for *nix](https://github.com/WhatDamon/WinSAT)

介绍：为 *nix 提供 Windows 风味的系统评测体验和体验指数

还原的部分：Windows 系统评估工具

- 许可证：WTFPL
- 作者：[WhatDamon](https://github.com/WhatDamon)
- 主要语言：zh-CN
- 支持语言：en-US / zh-CN
- 介绍视频：https://www.bilibili.com/video/BV1MegT68E15

### [Windows 搜索](https://github.com/WhatDamon/WindowsSearch) [整活]

介绍：将 Windows 上赤石的搜索体验带入 *nix 世界

还原的部分：Windows 的任务栏搜索与索引功能

- 许可证：WTFPL
- 作者：[WhatDamon](https://github.com/WhatDamon)
- 主要语言：zh-CN
- 支持语言：zh-CN
- 介绍视频：https://www.bilibili.com/video/BV1jruf6QEmh

### [Explorer-for-Linux](https://github.com/macOS-Terminal/Explorer-for-Linux) [整活]

介绍：在 Linux 上深度复刻 Win11 文件管理体验的桌面程序。

还原的部分：Win11 资源管理器界面（含经典「未响应」体验）。

- 许可证：未标注
- 作者：[macOS-Terminal](https://github.com/macOS-Terminal)
- 主要语言：zh-CN
- 支持语言：zh-CN
- 介绍视频：https://www.bilibili.com/video/BV1ZWgV68EtU

### [Explorer-for-Linux (xbodwf)](https://github.com/xbodwf/explorer-for-linux) [实用]

介绍：基于 Electron + Vue 与 WinUI 风格 Web 组件构建的 Win11 风格 Linux 文件管理器。

还原的部分：Win11 资源管理器的界面与使用体验（Fluent/WinUI 视觉风格）。

- 许可证：GPL-3.0
- 作者：[xbodwf](https://github.com/xbodwf)
- 主要语言：zh-CN
- 支持语言：zh-CN
- 介绍视频：（待补充）

### [mmclinux](https://gitee.com/windowsuninstaller/mmclinux) [实用]

介绍：仿 Windows 管理控制台的跨平台工具，基于 tkinter 实现。

还原的部分：MMC 管理控制台（MDI 子窗口、管理单元、窗口嵌套）。

- 许可证：MIT
- 作者：[WindowsUninstaller](https://gitee.com/windowsuninstaller)
- 主要语言：zh-CN
- 支持语言：zh-CN / en-US
- 介绍视频：https://www.bilibili.com/video/BV1gVuB6nEQk

### [NotepadOnLinux](https://github.com/linux-user-114514/NotepadOnLinux) [实用]

介绍：在 Linux 上还原 Windows 记事本的独立程序。

还原的部分：Windows 记事本（Notepad）界面。

- 许可证：未标注
- 作者：[linux-user-114514](https://github.com/linux-user-114514)
- 主要语言：zh-CN
- 支持语言：en-US / zh-CN
- 介绍视频：https://www.bilibili.com/video/BV1aigV6HETK

### [regedit](https://github.com/heyManNice/regedit) [实用]

介绍：把 `/etc`、`~/.config`、`/boot` 映射成注册表树、自动嗅探多种配置格式的系统配置文件浏览器。

还原的部分：注册表编辑器界面（左侧树 + 右侧键值）。

- 许可证：GPL-3.0（README 声明，未附 LICENSE 文件）
- 作者：[heyManNice](https://github.com/heyManNice)
- 主要语言：zh-CN
- 支持语言：zh-CN
- 介绍视频：https://www.bilibili.com/video/BV1CWuV6iEW6

### [runbox](https://github.com/HelloAIXIAOJI/runbox) [实用]

介绍：Linux 上按下 `Super+R` 弹出的运行对话框，Adwaita 外观随系统主题。

还原的部分：Win+R「运行」对话框。

- 许可证：MIT
- 作者：[HelloAIXIAOJI](https://github.com/HelloAIXIAOJI)
- 主要语言：zh-CN
- 支持语言：en-US / zh-CN
- 介绍视频：https://www.bilibili.com/video/BV1CxgJ6pEHr

### [SAS-for-Linux](https://github.com/macOS-Terminal/SAS-for-Linux)

介绍：用 C++/Qt 6 实现的 Windows 11 风格 Ctrl+Alt+Delete 安全选项屏，支持 X11 与 Wayland（GNOME/KDE/Sway/Hyprland/Niri）。

还原的部分：Windows 11 安全选项屏幕（锁定/切换用户/注销/更改密码/任务管理器 + 网络/无障碍/电源）。

- 许可证：未标注
- 作者：[macOS-Terminal](https://github.com/macOS-Terminal)
- 主要语言：zh-CN
- 支持语言：zh-CN
- 介绍视频：https://www.bilibili.com/video/BV1FQgn6sERt

## 系统交互

> 嵌入系统服务层的项目：PAM 模块、弹窗、全局热键。

### [adpop](https://github.com/MEKCCK/adpop) [整活]

介绍：完全自绘渲染、供其他软件调用的通用广告弹窗服务。

还原的部分：仿 Windows 流氓广告弹窗（动图 / 视频 / 音频 / 弹窗轰炸 / 流氓关闭）。

- 许可证：未标注
- 作者：[MEKCCK](https://github.com/MEKCCK)
- 主要语言：zh-CN
- 支持语言：zh-CN
- 介绍视频：https://www.bilibili.com/video/BV1ARgV6gEGm

### [libobscure](https://github.com/LyCecilion/libobscure) [整活]

介绍：将报错信息修改为 Windows 风格的错误代码。

还原的部分：Windows 风格的错误代码。

- 许可证：MIT
- 作者：[Limity'roChen](https://github.com/LyCecilion)
- 主要语言：zh-CN
- 支持语言：zh-CN / en-US
- 介绍视频：https://www.bilibili.com/video/BV1QVgc6UEcw/

### [libschrodinger](https://github.com/LyCecilion/libschrodinger)

介绍：在程序遇到致命错误时弹出「应用程序错误」对话框

还原的部分：「应用程序错误」对话框

- 许可证：MIT
- 作者：[Limity'roChen](https://github.com/LyCecilion)
- 主要语言：zh-CN
- 支持语言：zh-CN / en-US
- 介绍视频：https://www.bilibili.com/video/BV1Qag36jETo/

### [Linux_uac](https://github.com/WenAnrong/Linux_uac) [整活]

介绍：通过自定义 PAM 模块在 Linux 上复刻 Windows 的 UAC（用户账户控制）弹窗，sudo 时屏幕变暗冻结并弹出密码校验。

还原的部分：Windows UAC 用户账户控制弹窗（变暗冻结 + 密码校验 + 是/否 + 提示音）。

- 许可证：MIT
- 作者：[WenAnrong](https://github.com/WenAnrong)
- 主要语言：zh-CN
- 支持语言：en-US / zh-CN
- 介绍视频：https://www.bilibili.com/video/BV1qjgn6EErZ

## 底层 / 逆向

> 二进制格式与贴近内核的项目：DRM 直渲、PE/ELF、系统内部。

### [bsod](https://github.com/heyManNice/bsod) [整活]

介绍：在 Linux 物理屏上直接渲染、抢占 DRM Master 的蓝屏演示工具，支持多语言与日志监控。

还原的部分：Win10 蓝屏死机界面（含二维码）。

- 许可证：MIT
- 作者：[heyManNice](https://github.com/heyManNice)
- 主要语言：zh-CN
- 支持语言：en-US / zh-CN / zh-TW / ja / ko
- 介绍视频：https://www.bilibili.com/video/BV1xcuU6uEyw

### [LinuxForWindows](https://github.com/dyz131005/LinuxForWindows)

介绍：从文件格式层面把 Windows PE 可执行文件离线转换为 Linux ELF 的二进制转换工具。

还原的部分：PE / ELF 文件格式结构（头、节表、程序头、动态段）。

- 许可证：MIT
- 作者：[dyz131005](https://github.com/dyz131005)
- 主要语言：zh-CN
- 支持语言：zh-CN
- 介绍视频：https://www.bilibili.com/video/BV1p1gE6DEVF

### [windows_update_in_linux](https://github.com/WenAnrong/windows_update_in_linux) [整活]

介绍：伪 Windows 更新界面的整活程序，每次运行 50% 真更新重启、50% 蓝屏。

还原的部分：Windows 更新界面（成功进度 / 失败蓝屏）。

- 许可证：MIT
- 作者：[WenAnrong](https://github.com/WenAnrong)
- 主要语言：zh-CN
- 支持语言：en-US / zh-CN
- 介绍视频：https://www.bilibili.com/video/BV15iuR6zEBE

---

## 贡献

欢迎提交 PR 补充更多「Windows on Linux」项目。条目建议包含：项目链接、许可证、作者、主要 / 支持语言、一句话介绍、还原的部分。

### 创建自己的项目条目

运行 `python main.py new`，按提示选择组并输入项目名。脚本会生成项目目录（`new` 命令会打印生成路径），并在其中为每种语言创建 JSON 文件。

生成的目录结构：

```text
my-awesome-tool/
├── zh-CN.json
└── en-US.json
```

打开项目 JSON，填写字段：

```json
{
  "name": "my-awesome-tool",
  "intro": "",
  "restores": "",
  "license": "",
  "url": "",
  "authors": [],
  "lang_primary": "zh-CN",
  "lang_supported": ["zh-CN"],
  "intent": "practical"
}
```

| 字段 | 必填 | 说明 |
| --- | --- | --- |
| `name` | 是 | 项目显示名 |
| `url` | 是 | 项目仓库地址 |
| `intro` | 是 | 一句话介绍 |
| `restores` | 是 | 还原了 Windows 的哪个部分 |
| `license` | 是 | 开源许可证 |
| `authors` | 是 | 作者列表，每项含 `name` 与 `url` |
| `lang_primary` | 是 | 主要语言 |
| `lang_supported` | 是 | 支持的语言数组 |
| `video` | 否 | 介绍视频链接 |
| `intent` | 是 | 意图标签：`practical` / `prank` / `mixed` |

`intent` 与基于形态的分组正交：**practical** = 实用、可安全使用；**prank** = 整活、别在生产机跑；**mixed** = 两者兼具。

编辑完成后重新生成并校验：

```bash
python main.py generate
python main.py lint
```

然后提交并发起 Pull Request：

```bash
git add .
git commit -m "feat: add my-awesome-tool"
git push
```

创建 Pull Request，Actions 全部通过后才可合并。

### 常见问题

- **`lint` 报错**：运行 `python main.py check` 和 `python main.py cl` 定位具体问题。
- **语言不对称**：`project-meta/` 里有哪些语言，每个项目就要有哪些语言的 JSON。
- **删除条目**：删掉项目目录，再重新 `generate` 即可。

---

## 许可

[MIT](LICENSE) © 2026 windowix


*生成于: 2026-08-16 00:40 UTC*
