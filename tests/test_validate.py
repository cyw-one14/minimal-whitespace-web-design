import importlib.util
import tempfile
import unittest
from pathlib import Path

SPEC = importlib.util.spec_from_file_location("validate_skill", Path(__file__).resolve().parents[1] / "scripts" / "validate.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class PackageValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name) / "sample-skill"
        self.root.mkdir()
        (self.root / "agents").mkdir()
        (self.root / "SKILL.md").write_text(
            '---\nname: sample-skill\ndescription: "A useful sample skill"\nlicense: MIT\n---\n\n# Sample\n',
            encoding="utf-8",
        )
        (self.root / "agents" / "openai.yaml").write_text(
            'interface:\n  display_name: "Sample"\n  short_description: "A useful sample for package validation"\n  default_prompt: "Use $sample-skill to complete the task."\n',
            encoding="utf-8",
        )
        (self.root / "LICENSE").write_text("MIT License\n", encoding="utf-8")

    def tearDown(self):
        self.temp.cleanup()

    def test_valid_unicode_reference_resolves(self):
        (self.root / "guide.md").write_text("# Guide\n中文与日本語。", encoding="utf-8")
        with (self.root / "SKILL.md").open("a", encoding="utf-8") as file:
            file.write("\n[Guide](guide.md)\n")
        self.assertEqual(MODULE.validate(self.root), [])

    def test_missing_reference_fails(self):
        with (self.root / "SKILL.md").open("a", encoding="utf-8") as file:
            file.write("\n[Guide](missing.md)\n")
        self.assertTrue(any("does not resolve" in issue for issue in MODULE.validate(self.root)))

    def test_existing_reference_cannot_escape_package(self):
        (self.root.parent / "outside.md").write_text("# Outside", encoding="utf-8")
        with (self.root / "SKILL.md").open("a", encoding="utf-8") as file:
            file.write("\n[Outside](../outside.md)\n")
        self.assertTrue(any("escapes package" in issue for issue in MODULE.validate(self.root)))

    def test_stale_invocation_fails_after_rename(self):
        metadata = self.root / "agents" / "openai.yaml"
        metadata.write_text(metadata.read_text(encoding="utf-8").replace("$sample-skill", "$old-skill"), encoding="utf-8")
        self.assertTrue(any("does not invoke" in issue for issue in MODULE.validate(self.root)))

    def test_invalid_yaml_is_rejected(self):
        (self.root / "agents" / "openai.yaml").write_text("interface: [\n", encoding="utf-8")
        self.assertTrue(any("invalid" in issue.lower() for issue in MODULE.validate(self.root)))

    def test_default_prompt_suffix_is_rejected(self):
        metadata = self.root / "agents" / "openai.yaml"
        metadata.write_text(metadata.read_text(encoding="utf-8").replace("$sample-skill", "$sample-skill-extra"), encoding="utf-8")
        self.assertTrue(any("does not invoke" in issue for issue in MODULE.validate(self.root)))

    def test_stale_readme_invocation_is_rejected(self):
        (self.root / "README.md").write_text("```text\nUse $old-skill for the task.\n```\n", encoding="utf-8")
        self.assertTrue(any("invocation differs" in issue for issue in MODULE.validate(self.root)))

    def test_readme_environment_variables_remain_valid(self):
        (self.root / "README.md").write_text("Install using $HOME, $CODEX_HOME, $env:USERPROFILE or $skillRoot.\nUse $sample-skill.\n", encoding="utf-8")
        self.assertEqual(MODULE.validate(self.root), [])


if __name__ == "__main__":
    unittest.main()
