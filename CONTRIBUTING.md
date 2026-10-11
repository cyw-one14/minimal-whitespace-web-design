# Contributing

Keep the skill useful across brands and technology stacks. Add a rule when an observed failure or real requirement changes a decision, rather than turning every example into a universal constraint.

- Keep shared guidance in `SKILL.md`; load detailed references only when relevant.
- Keep naming, discovery metadata, and examples consistent.
- Retain visible content when animation, JavaScript, or image initialization fails.
- Explain behavioral changes and their validation. Tests should catch meaningful packaging or workflow failures.
- Do not submit client identities, local account paths, internal hosts, production settings, credentials, raw customer assets, or private chat excerpts. Use synthetic examples and authorized materials.

Before submitting, install `requirements-dev.txt`, run `python scripts/validate.py .` and `python -m unittest discover -s tests -v`, and review the exact Git diff. For workflow changes, also try a small realistic request and report the actual validation scope.

For confidential reports, use any private reporting channel the maintainer has enabled. Do not place sensitive values in public issues; if no private channel is available, report only a redacted description.
