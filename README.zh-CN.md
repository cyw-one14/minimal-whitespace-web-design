# Minimal Whitespace Web Design & Build

[English](README.md)

**简约留白网站设计与制作**：以真实内容为核心，采用大图、清晰排版和克制动效。颜色、字体、布局和技术栈根据当前品牌与项目调整。

适用于品牌官网、产品页面、作品集、服务网站和产品界面；按需要覆盖内容管理、多语言、响应式、SEO、测试及上线交付。高密度工具界面优先满足操作效率，不强制采用大图或沉浸章节。

## 安装与使用

将仓库放进代理的 skills 目录，文件夹名保持为 `minimal-whitespace-web-design`。Codex 配置了 `CODEX_HOME` 时使用其中的 `skills` 目录，否则使用用户目录下的 `.codex/skills`。其他代理按其自身说明安装。

可按 [英文 README 中的命令](README.md) 克隆，也可下载 GitHub ZIP 后解压、改成上述文件夹名并放入目录。已有同名安装时先保留自己的修改。技能发现与刷新方式由使用的代理决定。

```text
请使用 $minimal-whitespace-web-design，为我的品牌设计并制作网站。
沿用现有技术栈，结合我提供的素材调整颜色、字体、布局和动效。
```

本包是可复用的指导方法，不是独立建站软件。名称和发现信息使用英文，技能正文与详细参考使用中文；执行时按用户语言沟通。使用 skill 本身不需要安装 Python 或第三方库。

## 内容与检查

- [核心流程](SKILL.md)：需求、设计、制作和交付。
- [视觉与响应式](references/design-system.md)、[页面组织](references/page-patterns.md)、[素材与动效](references/motion-and-assets.md)。
- [内容与交付](references/build-and-delivery.md)：按需接入 CMS、多语言、SEO、离线交付和上线验证。
- [通用经验边界](references/design-lessons.md)、[公开发布审核](docs/release-review.md)。

维护人员使用 Python 3.10+ 执行结构与引用检查：

```sh
python -m pip install -r requirements-dev.txt
python scripts/validate.py .
python -m unittest discover -s tests -v
```

自动检查不能替代实际页面验收或人工隐私审核，具体范围见 [贡献说明](CONTRIBUTING.md)。

## 许可

[MIT](LICENSE)。许可覆盖此仓库的发布内容；使用外部品牌、素材和业务资料时仍需对应授权。
