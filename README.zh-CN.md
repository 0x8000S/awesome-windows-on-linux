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

- **文档**
  - [贡献](#贡献)
  - [创建自己的项目条目](#创建自己的项目条目)
  - [常见问题](#常见问题)
  - [许可](#许可)

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
- 介绍视频：https://www.bilibili.com/video/BV1LNgG69EMe

### [cmd](https://github.com/ChenPi11/cmd)

介绍：从零用纯 C89 忠实重写 Windows `cmd.exe` 的命令解释器，纯 POSIX 零依赖，能跑在任何 Unix 上。

还原的部分：Windows `cmd.exe` 命令行解释器（批处理、管道重定向、40+ 内置命令）。

- 许可证：GPL-3.0
- 作者：[ChenPi11](https://github.com/ChenPi11)
- 主要语言：en-US
- 支持语言：en-US / zh-CN / zh-MS / zh-WY
- 介绍视频：https://www.bilibili.com/video/BV1wkuH64EE8

### [runbox](https://github.com/HelloAIXIAOJI/runbox)

介绍：Linux 上按下 `Super+R` 弹出的运行对话框，Adwaita 外观随系统主题。

还原的部分：Win+R「运行」对话框。

- 许可证：MIT
- 作者：[HelloAIXIAOJI](https://github.com/HelloAIXIAOJI)
- 主要语言：en-US
- 支持语言：en-US / zh-CN
- 介绍视频：https://www.bilibili.com/video/BV1CxgJ6pEHr

### [Windowshit](https://github.com/HelloAIXIAOJI/windowshit)

介绍：用 Rust 重写的 Windows 命令行工具合集，跨平台运行。

还原的部分：24 个 Windows 命令行工具（ipconfig / ping / robocopy / systeminfo…）。

- 许可证：MIT
- 作者：[HelloAIXIAOJI](https://github.com/HelloAIXIAOJI)
- 主要语言：en-US
- 支持语言：en-US / zh-CN
- 介绍视频：https://www.bilibili.com/video/BV1Pzuy6oEZm

## 硬核逆向 / 底层格式

> 正经技术项目

### [LinuxForWindows](https://github.com/dyz131005/LinuxForWindows)

介绍：从文件格式层面把 Windows PE 可执行文件离线转换为 Linux ELF 的二进制转换工具。

还原的部分：PE / ELF 文件格式结构（头、节表、程序头、动态段）。

- 许可证：MIT
- 作者：[dyz131005](https://github.com/dyz131005)
- 主要语言：zh-CN
- 支持语言：zh-CN
- 介绍视频：https://www.bilibili.com/video/BV1p1gE6DEVF

## GUI 复刻

> 复刻 Windows 桌面 GUI 体验。

### [Explorer-for-Linux](https://github.com/macOS-Terminal/Explorer-for-Linux)

介绍：在 Linux 上深度复刻 Win11 文件管理体验的桌面程序。

还原的部分：Win11 资源管理器界面（含经典「未响应」体验）。

- 许可证：未标注
- 作者：[macOS-Terminal](https://github.com/macOS-Terminal)
- 主要语言：zh-CN
- 支持语言：zh-CN
- 介绍视频：https://www.bilibili.com/video/BV1ZWgV68EtU

### [mmclinux](https://gitee.com/windowsuninstaller/mmclinux)

介绍：仿 Windows 管理控制台的跨平台工具，基于 tkinter 实现。

还原的部分：MMC 管理控制台（MDI 子窗口、管理单元、窗口嵌套）。

- 许可证：MIT
- 作者：[WindowsUninstaller](https://gitee.com/windowsuninstaller)
- 主要语言：zh-CN
- 支持语言：zh-CN / en-US
- 介绍视频：https://www.bilibili.com/video/BV1gVuB6nEQk

### [regedit](https://github.com/heyManNice/regedit)

介绍：把 `/etc`、`~/.config`、`/boot` 映射成注册表树、自动嗅探多种配置格式的系统配置文件浏览器。

还原的部分：注册表编辑器界面（左侧树 + 右侧键值）。

- 许可证：GPL-3.0（README 声明，未附 LICENSE 文件）
- 作者：[heyManNice](https://github.com/heyManNice)
- 主要语言：zh-CN
- 支持语言：zh-CN
- 介绍视频：https://www.bilibili.com/video/BV1CWuV6iEW6

## 整活恶搞

> 纯整活，别在生产机器上乱跑。

### [adpop](https://github.com/MEKCCK/adpop)

介绍：完全自绘渲染、供其他软件调用的通用广告弹窗服务。

还原的部分：仿 Windows 流氓广告弹窗（动图 / 视频 / 音频 / 弹窗轰炸 / 流氓关闭）。

- 许可证：未标注
- 作者：[MEKCCK](https://github.com/MEKCCK)
- 主要语言：zh-CN
- 支持语言：zh-CN
- 介绍视频：https://www.bilibili.com/video/BV1ARgV6gEGm

### [bsod](https://github.com/heyManNice/bsod)

介绍：在 Linux 物理屏上直接渲染、抢占 DRM Master 的蓝屏演示工具，支持多语言与日志监控。

还原的部分：Win10 蓝屏死机界面（含二维码）。

- 许可证：MIT
- 作者：[heyManNice](https://github.com/heyManNice)
- 主要语言：en-US
- 支持语言：en-US / zh-CN / zh-TW / ja / ko
- 介绍视频：https://www.bilibili.com/video/BV1xcuU6uEyw

### [windows_update_in_linux](https://github.com/WenAnrong/windows_update_in_linux)

介绍：伪 Windows 更新界面的整活程序，每次运行 50% 真更新重启、50% 蓝屏。

还原的部分：Windows 更新界面（成功进度 / 失败蓝屏）。

- 许可证：MIT
- 作者：[WenAnrong](https://github.com/WenAnrong)
- 主要语言：en-US
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
  "lang_supported": ["zh-CN"]
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


*生成于: 2026-08-13 14:33 UTC*
