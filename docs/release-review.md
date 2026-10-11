# Public release review

Release scope: reusable website-design instructions, generic CSS examples, Agent Skill metadata, and maintenance checks.

## Privacy boundary

The public package generalizes project experience. It contains no source-project names, personal workstation paths, private knowledge-base locations, customer contacts, unpublished business metrics, deployment hostnames, credentials, production configuration, or raw business assets.

An independent content review and a local pre-release scan cover the selected publication files. The scan is a supporting check, not a proof that every possible future contribution is safe to publish. Review the actual diff and any new Git history before release.

Only a fresh history for the reviewed package is published. The maintainer's public GitHub handle is used for attribution; commit metadata uses the GitHub noreply address. Private development notes, source snapshots, trial artifacts, and publishing credentials are outside the release.

## Validation scope

Release checks cover skill frontmatter, invocation consistency, UTF-8, YAML, local-reference containment and resolution, and the validator's negative cases. GitHub Actions runs the same maintenance checks on pushes and pull requests.

A prior anonymous offline service-site exercise validated local loading, nine viewport widths, navigation, keyboard interaction, reduced motion, and navigation with JavaScript disabled. That exercise supports the design workflow; it does not establish that future generated websites, live HTTP routes, databases, deployment environments, or physical touch devices have been verified.

This repository distributes instructions rather than a running website. Actual projects still need their own content, accessibility, browser, integration, and deployment checks.

## Distribution

The repository is licensed under MIT. The license covers the published files only. External projects, brands, images, and data require their own authorization. Development dependencies and GitHub Actions are referenced rather than bundled.
