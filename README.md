# Awesome Windows on Linux (Only funny)

<p align="center"><img src="awologo.png" alt="Awesome Windows on Linux Logo" width="520"></p>

> A collection of projects that bring the Windows experience to Linux — from hardcore reverse engineering to hilarious pranks.

**en-US** | [zh-CN](README.zh-CN.md)

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

This list collects open-source projects that replicate, simulate, or parody the Windows ecosystem on Linux. Projects are grouped by **form** (CLI tools, GUI apps, system interaction, low-level/reverse engineering), and each carries an **intent tag** — `[Practical]` for things you can actually use, `[Prank]` for things you should not run on a production machine.

---

## Contents

- [Info](#info)
- [CLI Tools](#cli-tools)
- [GUI Applications](#gui-applications)
- [System Interaction](#system-interaction)
- [Low-level / Reverse Engineering](#low-level--reverse-engineering)

- **Docs**
  - [Contribute](#contribute)
  - [Create your own project entry](#create-your-own-project-entry)
  - [Troubleshooting](#troubleshooting)
  - [License](#license)

---

## Info

> I don't know what to put here either, haha.

### [Awesome Windows on Linux](https://github.com/windowix/awesome-windows-on-linux)

Intro: A curated collection of open-source projects that replicate, simulate, or parody the Windows ecosystem on Linux.

Restores: Curating and organizing projects that recreate Windows.

- License: MIT
- Authors: [windowix](https://github.com/windowix), [HelloAIXIAOJI](https://github.com/HelloAIXIAOJI)
- Primary language: en-US
- Supported languages: en-US / zh-CN
- Intro video: https://www.bilibili.com/video/BV1mMgs6gET6

## CLI Tools

> Command-line tools that restore Windows terminal commands on Unix.

### [aptx](https://github.com/WenAnrong/aptx)

Intro: An enhanced apt wrapper that recommends similar software after installing/removing packages.

Restores: The 'bundleware recommendations' nuisance experience when installing software.

- License: MIT
- Authors: [WenAnrong](https://github.com/WenAnrong)
- Primary language: en-US
- Supported languages: en-US / zh-CN
- Intro video: https://www.bilibili.com/video/BV1LNgG69EMe

### [cmd](https://github.com/ChenPi11/cmd) [Practical]

Intro: A faithful reimplementation of Windows `cmd.exe` written from scratch in pure C89, with zero POSIX dependencies, running on any Unix.

Restores: The Windows `cmd.exe` command interpreter (batch scripting, pipes/redirection, 40+ built-in commands).

- License: GPL-3.0
- Authors: [ChenPi11](https://github.com/ChenPi11)
- Primary language: en-US
- Supported languages: en-US / zh-CN / zh-MS / zh-WY
- Intro video: https://www.bilibili.com/video/BV1wkuH64EE8

### [Windowshit](https://github.com/HelloAIXIAOJI/windowshit) [Practical]

Intro: A collection of Windows command-line tools rewritten in Rust, running cross-platform.

Restores: 24 Windows command-line tools (ipconfig / ping / robocopy / systeminfo...).

- License: MIT
- Authors: [HelloAIXIAOJI](https://github.com/HelloAIXIAOJI)
- Primary language: en-US
- Supported languages: en-US / zh-CN
- Intro video: https://www.bilibili.com/video/BV1Pzuy6oEZm

## GUI Applications

> Graphical apps that recreate Windows desktop interfaces.

### [Explorer-for-Linux](https://github.com/macOS-Terminal/Explorer-for-Linux) [Prank]

Intro: A desktop program that deeply replicates the Win11 file-management experience on Linux.

Restores: The Win11 File Explorer interface (including the classic 'Not Responding' experience).

- License: Unspecified
- Authors: [macOS-Terminal](https://github.com/macOS-Terminal)
- Primary language: zh-CN
- Supported languages: zh-CN
- Intro video: https://www.bilibili.com/video/BV1ZWgV68EtU

### [mmclinux](https://gitee.com/windowsuninstaller/mmclinux) [Practical]

Intro: A cross-platform tool mimicking the Windows Management Console, built with tkinter.

Restores: The MMC console (MDI child windows, snap-ins, window embedding).

- License: MIT
- Authors: [WindowsUninstaller](https://gitee.com/windowsuninstaller)
- Primary language: zh-CN
- Supported languages: zh-CN / en-US
- Intro video: https://www.bilibili.com/video/BV1gVuB6nEQk

### [NotepadOnLinux](https://github.com/linux-user-114514/NotepadOnLinux) [Practical]

Intro: A standalone program that recreates Windows Notepad on Linux.

Restores: The Windows Notepad interface.

- License: Unspecified
- Authors: [linux-user-114514](https://github.com/linux-user-114514)
- Primary language: en-US
- Supported languages: en-US
- Intro video: https://www.bilibili.com/video/BV1aigV6HETK

### [regedit](https://github.com/heyManNice/regedit) [Practical]

Intro: A system configuration file browser that maps `/etc`, `~/.config`, and `/boot` to a registry tree and auto-detects multiple config formats.

Restores: The registry editor interface (left tree + right key/value list).

- License: GPL-3.0 (declared in README; no LICENSE file shipped)
- Authors: [heyManNice](https://github.com/heyManNice)
- Primary language: zh-CN
- Supported languages: zh-CN
- Intro video: https://www.bilibili.com/video/BV1CWuV6iEW6

### [runbox](https://github.com/HelloAIXIAOJI/runbox) [Practical]

Intro: A run dialog on Linux that pops up with `Super+R`, with an Adwaita look following the system theme.

Restores: The Win+R 'Run' dialog.

- License: MIT
- Authors: [HelloAIXIAOJI](https://github.com/HelloAIXIAOJI)
- Primary language: en-US
- Supported languages: en-US / zh-CN
- Intro video: https://www.bilibili.com/video/BV1CxgJ6pEHr

### [SAS-for-Linux](https://github.com/macOS-Terminal/SAS-for-Linux)

Intro: A Windows 11-style Ctrl+Alt+Delete secure attention screen implemented in C++/Qt 6, supporting X11 and Wayland (GNOME/KDE/Sway/Hyprland/Niri).

Restores: The Windows 11 secure attention screen (lock / switch user / log out / change password / task manager + network / accessibility / power).

- License: Unspecified
- Authors: [macOS-Terminal](https://github.com/macOS-Terminal)
- Primary language: zh-CN
- Supported languages: zh-CN
- Intro video: https://www.bilibili.com/video/BV1FQgn6sERt

## System Interaction

> Projects that hook into system services: PAM modules, popups, global hotkeys.

### [adpop](https://github.com/MEKCCK/adpop) [Prank]

Intro: A general-purpose ad-popup service rendered fully from scratch, callable by other software.

Restores: Windows-style malicious ad popups (animated images / video / audio / popup spam / non-closable).

- License: Unspecified
- Authors: [MEKCCK](https://github.com/MEKCCK)
- Primary language: zh-CN
- Supported languages: zh-CN
- Intro video: https://www.bilibili.com/video/BV1ARgV6gEGm

### [Linux_uac](https://github.com/WenAnrong/Linux_uac) [Prank]

Intro: Recreates Windows UAC (User Account Control) on Linux via a custom PAM module: the screen dims and freezes, then a password prompt appears when you run sudo.

Restores: The Windows UAC dialog (dim & freeze + password check + Yes/No + chime).

- License: MIT
- Authors: [WenAnrong](https://github.com/WenAnrong)
- Primary language: en-US
- Supported languages: en-US
- Intro video: https://www.bilibili.com/video/BV1qjgn6EErZ

## Low-level / Reverse Engineering

> Binary-format and kernel-adjacent projects: DRM rendering, PE/ELF, system internals.

### [bsod](https://github.com/heyManNice/bsod) [Prank]

Intro: A blue-screen demo tool that renders directly on the Linux physical display, grabbing DRM Master, with multi-language and log monitoring.

Restores: The Win10 Blue Screen of Death interface (with QR code).

- License: MIT
- Authors: [heyManNice](https://github.com/heyManNice)
- Primary language: en-US
- Supported languages: en-US / zh-CN / zh-TW / ja / ko
- Intro video: https://www.bilibili.com/video/BV1xcuU6uEyw

### [LinuxForWindows](https://github.com/dyz131005/LinuxForWindows)

Intro: A binary conversion tool that offline-converts Windows PE executables into Linux ELF at the file-format level.

Restores: PE / ELF file format structures (header, section table, program headers, dynamic segment).

- License: MIT
- Authors: [dyz131005](https://github.com/dyz131005)
- Primary language: zh-CN
- Supported languages: zh-CN
- Intro video: https://www.bilibili.com/video/BV1p1gE6DEVF

### [windows_update_in_linux](https://github.com/WenAnrong/windows_update_in_linux) [Prank]

Intro: A prank program showing a fake Windows update screen: 50% chance of a real update+reboot, 50% chance of a blue screen.

Restores: The Windows update screen (success progress / failure blue screen).

- License: MIT
- Authors: [WenAnrong](https://github.com/WenAnrong)
- Primary language: en-US
- Supported languages: en-US / zh-CN
- Intro video: https://www.bilibili.com/video/BV15iuR6zEBE

---

## Contribute

Welcome to submit PRs to add more "Windows on Linux" projects. Each entry should include: project link, license, authors, primary/supported languages, a one-line intro, and what Windows part it restores.

### Create your own project entry

Run `python main.py new`, pick a group, and enter a project name when prompted. The script creates the project directory (it prints the generated path) with one JSON file per language.

Generated directory structure:

```text
my-awesome-tool/
├── zh-CN.json
└── en-US.json
```

Open the project JSON and fill in the fields:

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

| Field | Required | Description |
| --- | --- | --- |
| `name` | yes | Project display name |
| `url` | yes | Repository URL |
| `intro` | yes | One-line intro |
| `restores` | yes | Which Windows part it restores |
| `license` | yes | Open-source license |
| `authors` | yes | List of authors, each with `name` and `url` |
| `lang_primary` | yes | Primary language |
| `lang_supported` | yes | Array of supported languages |
| `video` | no | Intro video link |
| `intent` | yes | Intent tag: `practical` / `prank` / `mixed` |

`intent` is orthogonal to the form-based group: **practical** = usable/safe, **prank** = parody/not for production, **mixed** = both.

After editing, regenerate and validate:

```bash
python main.py generate
python main.py lint
```

Then commit and open a Pull Request:

```bash
git add .
git commit -m "feat: add my-awesome-tool"
git push
```

Create the Pull Request; it merges once all Actions pass.

### Troubleshooting

- **`lint` fails**: run `python main.py check` and `python main.py cl` to locate the issue.
- **Language asymmetry**: each project must have a JSON file for every language present in `project-meta/`.
- **Removing an entry**: delete the project directory, then re-run `generate`.

---

## License

[MIT](LICENSE) © 2026 windowix


*Generated at: 2026-08-13 18:20 UTC*
