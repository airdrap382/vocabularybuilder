"""Minimal example for VocabularyBuilder."""

from vocabularybuilder import vocabularybuilder


def main():
 runner = vocabularybuilder({"name": "VocabularyBuilder", "dry_run": False})
 result = runner.execute()
 print(result)


if __name__ == "__main__":
 main()