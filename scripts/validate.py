"""Validate a filesystem Agent Skill and its public-package references."""
from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

import yaml

EXCLUDED = {".git", ".venv", "__pycache__", ".cache"}


def validate(root: Path) -> list[str]:
    root = root.resolve()
    errors: list[str] = []
    entry = root / "SKILL.md"
    if not entry.is_file():
        return ["SKILL.md is missing"]

    try:
        source = entry.read_text(encoding="utf-8")
    except UnicodeError:
        return ["SKILL.md is not UTF-8"]
    front = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)", source, re.S)
    if not front:
        return ["SKILL.md has no valid YAML frontmatter"]
    try:
        data = yaml.safe_load(front.group(1))
    except yaml.YAMLError:
        return ["SKILL.md frontmatter is invalid YAML"]
    if not isinstance(data, dict):
        return ["SKILL.md frontmatter must be a mapping"]
    name = data.get("name", "")
    if not isinstance(name, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or len(name) > 64:
        errors.append("Invalid skill name")
        name = ""
    elif root.name != name:
        errors.append("Folder name differs from skill name")
    description = data.get("description", "")
    if not isinstance(description, str) or not description.strip() or len(description) > 1024:
        errors.append("Invalid skill description")
    if data.get("license") != "MIT" or not (root / "LICENSE").is_file():
        errors.append("MIT license declaration or LICENSE file is missing")

    metadata = root / "agents" / "openai.yaml"
    try:
        ui = yaml.safe_load(metadata.read_text(encoding="utf-8"))
        interface = ui["interface"]
        short = interface["short_description"]
        prompt = interface["default_prompt"]
        if not isinstance(interface["display_name"], str) or not interface["display_name"].strip():
            errors.append("Missing display name")
        if not isinstance(short, str) or not 25 <= len(short) <= 64:
            errors.append("Short description must contain 25-64 characters")
        prompt_names = re.findall(r"\$([A-Za-z0-9_-]+)", prompt) if isinstance(prompt, str) else []
        if not name or not prompt_names or any(token != name for token in prompt_names):
            errors.append("Default prompt does not invoke the named skill")
        policy = ui.get("policy", {})
        if "allow_implicit_invocation" in policy and not isinstance(policy["allow_implicit_invocation"], bool):
            errors.append("Invocation policy must be a boolean")
    except (OSError, UnicodeError, yaml.YAMLError, KeyError, TypeError):
        errors.append("Invalid or missing agents/openai.yaml")

    for path in root.rglob("*"):
        relative = path.relative_to(root)
        if set(relative.parts) & EXCLUDED:
            continue
        if path.is_symlink():
            errors.append(f"{relative}: symlink is outside the text-only package contract")
            continue
        if not path.is_file() or path.suffix.lower() not in {".md", ".yaml", ".yml", ".py", ".txt"}:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeError:
            errors.append(f"{relative}: not UTF-8")
            continue
        if text.startswith("\ufeff") or "\ufffd" in text:
            errors.append(f"{relative}: BOM or replacement character")
        if path.suffix.lower() in {".yaml", ".yml"}:
            try:
                yaml.safe_load(text)
            except yaml.YAMLError:
                errors.append(f"{relative}: invalid YAML")
        if path.suffix.lower() != ".md":
            continue
        for invocation in re.finditer(r"\$([A-Za-z0-9_-]+)", text):
            token = invocation.group(1)
            prefix = text[max(0, invocation.start() - 20):invocation.start()]
            explicit_use = re.search(r"(?:\buse|使用)\s*$", prefix, flags=re.I)
            if ("-" in token or token == name or explicit_use) and token != name:
                errors.append(f"{relative}: invocation differs from skill name")
        # Only inspect prose; a validator example may legitimately show scaffold syntax.
        prose = re.sub(r"(?ms)^\s*(`{3,}|~{3,})[^\n]*\n.*?^\s*\1\s*$", "", text)
        if re.search(r"(?m)^\s*\[TODO:[^\n]*\]\s*$", prose):
            errors.append(f"{relative}: unfinished scaffold")
        for raw in re.findall(r"!?\[[^\]\n]*\]\(([^)\n]+)\)", prose):
            target = raw.strip().strip("<>")
            parts = urlsplit(target)
            if parts.scheme or parts.netloc:
                if parts.scheme not in {"http", "https", "mailto"}:
                    errors.append(f"{relative}: unsupported link scheme")
                continue
            if not parts.path:
                continue
            local = (path.parent / unquote(parts.path)).resolve()
            if not local.is_relative_to(root):
                errors.append(f"{relative}: local link escapes package")
            elif not local.is_file():
                errors.append(f"{relative}: local link does not resolve")
    return errors


if __name__ == "__main__":
    directory = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
    problems = validate(directory)
    if problems:
        print("\n".join(problems))
        sys.exit(1)
    print("Skill metadata, UTF-8, YAML, invocation, and local links are valid.")
