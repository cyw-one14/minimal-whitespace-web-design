# Minimal Whitespace Web Design & Build

[中文说明](README.zh-CN.md)

An Agent Skill for designing and building websites around **authentic visuals, purposeful whitespace, clear typography, and restrained motion**.

Use it for brand sites, product pages, portfolios, service websites, and product interfaces. Adapt the palette, type, layout, density, and technology to the project. It supports content integration, optional CMS and localization, responsive behavior, and verified delivery without requiring a particular framework.

## Install

Place this repository in a folder named `minimal-whitespace-web-design` inside your agent's skills directory. For Codex, use `$CODEX_HOME/skills` when configured, or `~/.codex/skills` otherwise. Other agents should use their own documented skill location.

macOS / Linux:

```sh
git clone https://github.com/cyw-one14/minimal-whitespace-web-design.git \
  "${CODEX_HOME:-$HOME/.codex}/skills/minimal-whitespace-web-design"
```

Windows PowerShell:

```powershell
$skillRoot = if ($env:CODEX_HOME) {
  Join-Path $env:CODEX_HOME 'skills'
} else {
  Join-Path $env:USERPROFILE '.codex\skills'
}
git clone https://github.com/cyw-one14/minimal-whitespace-web-design.git `
  (Join-Path $skillRoot 'minimal-whitespace-web-design')
```

You can also download the repository ZIP, extract it, rename the extracted folder to `minimal-whitespace-web-design`, and place it in the same location. Do not overwrite an existing customized installation. Skill discovery depends on the host agent's refresh behavior.

## Use

```text
Use $minimal-whitespace-web-design to design and build a service website.
Use warm white and forest green, my approved content, and the existing stack.
```

```text
Use $minimal-whitespace-web-design to refine this product catalog.
Keep the existing design system and scope the changes to the card layout.
```

```text
请使用 $minimal-whitespace-web-design，为我的品牌设计并制作网站。
根据现有素材和技术栈调整颜色、字体、布局与动效。
```

This skill supplies instructions, not a standalone website generator. It has no runtime dependencies; the agent uses the tools and project environment available to it. The skill guide and detailed references are written in Chinese, with English discovery metadata. Respond in the user's language.

## Package

- [SKILL.md](SKILL.md): workflow, principles, scope, and selective reference loading.
- [Design system](references/design-system.md): brand adaptation, composition, type, and responsive boundaries.
- [Page patterns](references/page-patterns.md): navigation and page responsibilities.
- [Motion and assets](references/motion-and-assets.md): visible-first enhancement, real layout rows, media, and scrolling.
- [Build and delivery](references/build-and-delivery.md): content, CMS, localization, SEO, offline delivery, verification, and publishing.
- [Design lessons](references/design-lessons.md): generalized experience and limits.
- [Privacy and release review](docs/release-review.md): scope of the public-package review.

## Maintain and validate

Python 3.10+ is needed only for maintainers' checks:

```sh
python -m pip install -r requirements-dev.txt
python scripts/validate.py .
python -m unittest discover -s tests -v
```

The validator checks YAML metadata, invocation consistency, UTF-8, unfinished scaffolds, and local link containment/resolution. It does not prove visual quality or the absence of every possible sensitive fact. Review actual changes before release. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

[MIT](LICENSE). The license covers the contents of this repository; external brand assets, customer data, and project materials require their own authorization.
