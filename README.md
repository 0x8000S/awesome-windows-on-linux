# Awesome Windows on Linux (Only funny)

> A collection of projects that bring the Windows experience to Linux — from hardcore reverse engineering to hilarious pranks.

**en-US** | [zh-CN](README.zh-CN.md)

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

This list collects open-source projects that replicate, simulate, or parody the Windows ecosystem on Linux. Sorted roughly by 'fun factor', grouped into four categories: **hardcore reverse engineering**, **practical tools**, **GUI replicas**, and **pranks**.

---

## Contents

- [Practical Tools](#practical-tools)
- [Hardcore Reverse Engineering](#hardcore-reverse-engineering)
- [GUI Replicas](#gui-replicas)
- [Pranks](#pranks)

---

## Practical Tools

> Bring the Windows toolchain to Linux — the 'Swiss Army Knife'.

### [aptx](https://github.com/WenAnrong/aptx)

Intro: An enhanced apt wrapper that recommends similar software after installing/removing packages.

Restores: The 'bundleware recommendations' nuisance experience when installing software.

- License: MIT
- Authors: [WenAnrong](https://github.com/WenAnrong)
- Primary language: en-US
- Supported languages: en-US / zh-CN
- Intro video: (pending)

### [cmd](https://github.com/ChenPi11/cmd)

Intro: A faithful reimplementation of Windows `cmd.exe` written from scratch in pure C89, with zero POSIX dependencies, running on any Unix.

Restores: The Windows `cmd.exe` command interpreter (batch scripting, pipes/redirection, 40+ built-in commands).

- License: GPL-3.0
- Authors: [ChenPi11](https://github.com/ChenPi11)
- Primary language: en-US
- Supported languages: en-US / zh-CN / zh-MS / zh-WY
- Intro video: (pending)

### [runbox](https://github.com/HelloAIXIAOJI/runbox)

Intro: A run dialog on Linux that pops up with `Super+R`, with an Adwaita look following the system theme.

Restores: The Win+R 'Run' dialog.

- License: MIT
- Authors: [HelloAIXIAOJI](https://github.com/HelloAIXIAOJI)
- Primary language: en-US
- Supported languages: en-US / zh-CN
- Intro video: (pending)

### [Windowshit](https://github.com/HelloAIXIAOJI/windowshit)

Intro: A collection of Windows command-line tools rewritten in Rust, running cross-platform.

Restores: 24 Windows command-line tools (ipconfig / ping / robocopy / systeminfo...).

- License: MIT
- Authors: [HelloAIXIAOJI](https://github.com/HelloAIXIAOJI)
- Primary language: en-US
- Supported languages: en-US / zh-CN
- Intro video: (pending)

## Hardcore Reverse Engineering

> Serious tech projects: how Windows programs can survive on Linux.

### [LinuxForWindows](https://github.com/dyz131005/LinuxForWindows)

Intro: A binary conversion tool that offline-converts Windows PE executables into Linux ELF at the file-format level.

Restores: PE / ELF file format structures (header, section table, program headers, dynamic segment).

- License: MIT
- Authors: [dyz131005](https://github.com/dyz131005)
- Primary language: zh-CN
- Supported languages: zh-CN
- Intro video: (pending)

## GUI Replicas

> Replicate the Windows desktop GUI experience.

### [Explorer-for-Linux](https://github.com/macOS-Terminal/Explorer-for-Linux)

Intro: A desktop program that deeply replicates the Win11 file-management experience on Linux.

Restores: The Win11 File Explorer interface (including the classic 'Not Responding' experience).

- License: Unspecified
- Authors: [macOS-Terminal](https://github.com/macOS-Terminal)
- Primary language: zh-CN
- Supported languages: zh-CN
- Intro video: (pending)

### [mmclinux](https://gitee.com/windowsuninstaller/mmclinux)

Intro: A cross-platform tool mimicking the Windows Management Console, built with tkinter.

Restores: The MMC console (MDI child windows, snap-ins, window embedding).

- License: MIT
- Authors: [WindowsUninstaller](https://gitee.com/windowsuninstaller)
- Primary language: zh-CN
- Supported languages: zh-CN / en-US
- Intro video: (pending)

### [regedit](https://github.com/heyManNice/regedit)

Intro: A system configuration file browser that maps `/etc`, `~/.config`, and `/boot` to a registry tree and auto-detects multiple config formats.

Restores: The registry editor interface (left tree + right key/value list).

- License: GPL-3.0 (declared in README; no LICENSE file shipped)
- Authors: [heyManNice](https://github.com/heyManNice)
- Primary language: zh-CN
- Supported languages: zh-CN
- Intro video: (pending)

## Pranks

> Pure fun — don't run these on production machines.

### [adpop](https://github.com/MEKCCK/adpop)

Intro: A general-purpose ad-popup service rendered fully from scratch, callable by other software.

Restores: Windows-style malicious ad popups (animated images / video / audio / popup spam / non-closable).

- License: Unspecified
- Authors: [MEKCCK](https://github.com/MEKCCK)
- Primary language: zh-CN
- Supported languages: zh-CN
- Intro video: (pending)

### [bsod](https://github.com/heyManNice/bsod)

Intro: A blue-screen demo tool that renders directly on the Linux physical display, grabbing DRM Master, with multi-language and log monitoring.

Restores: The Win10 Blue Screen of Death interface (with QR code).

- License: MIT
- Authors: [heyManNice](https://github.com/heyManNice)
- Primary language: en-US
- Supported languages: en-US / zh-CN / zh-TW / ja / ko
- Intro video: (pending)

### [windows_update_in_linux](https://github.com/WenAnrong/windows_update_in_linux)

Intro: A prank program showing a fake Windows update screen: 50% chance of a real update+reboot, 50% chance of a blue screen.

Restores: The Windows update screen (success progress / failure blue screen).

- License: MIT
- Authors: [WenAnrong](https://github.com/WenAnrong)
- Primary language: en-US
- Supported languages: en-US / zh-CN
- Intro video: (pending)

---

## Contribute

Welcome to submit PRs to add more "Windows on Linux" projects. Each entry should include: project link, license, authors, primary/supported languages, a one-line intro, and what Windows part it restores.

### Create your own project entry

Want to add your project? The easiest way is to auto-generate the entry skeleton with the interactive command, then fill in the details.

### 1. Interactive creation

Run:

```bash
python main.py new
```

Follow the prompts:

1. **Pick a group**: enter the group number from the list (e.g. type `1` for "Practical Tools").
2. **Enter a project name**: an English ID; only letters, digits, hyphens `-`, and underscores `_` are allowed, and it must not start with a hyphen/underscore (e.g. `my-awesome-tool`).
3. **Auto-generate**: the script creates one JSON file per language (based on the `project-meta/` language set) under `project-datas/<group-id>/<project-name>/`.

### 2. Generated directory structure

```text
project-datas/
├── 1utilities/                  # group dir (numeric prefix controls order)
│   ├── awol-group-metadata/     # group metadata (name, note)
│   │   ├── zh-CN.json
│   │   └── en-US.json
│   └── my-awesome-tool/         # your project dir
│       ├── zh-CN.json
│       └── en-US.json
└── ...
```

### 3. Fill in the fields

Open the generated project JSON (e.g. `my-awesome-tool/zh-CN.json`). It starts like this:

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

| Field | Required | Description |
| --- | --- | --- |
| `name` | ✅ | Display name of the project |
| `url` | ✅ | Repository URL |
| `intro` | ✅ | One-line intro (what this project does) |
| `restores` | ✅ | Which Windows part it restores (keep separate from `intro`) |
| `license` | ✅ | Open-source license (e.g. `MIT`, `GPL-3.0`) |
| `authors` | ✅ | Array of authors, each with `name` (GitHub username) and `url` |
| `lang_primary` | ✅ | Primary language (most used by maintainers) |
| `lang_supported` | ✅ | Array of supported languages |
| `video` | ⬜ | Intro video link (can be empty; shows "pending") |

> Tip: `intro` describes "what the project itself is", while `restores` describes "which Windows part it replicates" — don't mix them.

### 4. Regenerate and validate

After editing, regenerate the READMEs and run validation:

```bash
python main.py generate --lang zh-CN   # regenerate Chinese README
python main.py generate --lang en-US   # regenerate English README
python main.py lint                    # full validation (lint = cl + check)
python main.py check                   # only check missing/extra fields
python main.py cl                      # only check language symmetry
```

Make sure `lint` prints `OK - no issues` before committing.

### 5. Commit & PR

```bash
git add .
git commit -m "feat: add my-awesome-tool"
git push
```

Then open a Pull Request. CI runs `lint` (including `check` and `cl`) plus a reproducibility check on the PR automatically; everything must pass to merge.

### Troubleshooting

- **`lint` fails**: usually a missing field or language asymmetry. Run `python main.py check` and `python main.py cl` to locate the issue.
- **Language asymmetry**: if `project-meta/` contains `en-US`, every project must have both `en-US.json` and `zh-CN.json` — not just one.
- **Removing an entry**: delete the whole `project-datas/<group-id>/<project-name>/` directory, then re-run `generate`.

---

## License

[MIT](LICENSE) © 2026 windowix


*Generated at: 2026-08-13 14:00 UTC*
