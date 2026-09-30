#!/usr/bin/env python3
from pathlib import Path
import sys

root = Path(__file__).resolve().parents[1]
required = [
    "README.md",
    "START_HERE.md",
    "LICENSE.md",
    "NOTICE.md",
    "PROMPTJECT_INDEX.md",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "FREE_AND_OPEN_USE.md",
    "prompts/SOCIAL_SERVICE_FORM_SHORTENER_MASTER_PROMPT.md",
    "prompts/COMPACT_EXECUTION_PROMPT.md",
    "prompts/PROMPT_ATOMIC_CORPUS.md",
]
missing = [p for p in required if not (root / p).exists()]
if missing:
    print("Missing required files:", ", ".join(missing))
    sys.exit(1)

license_text = (root / "LICENSE.md").read_text(encoding="utf-8")
if "Wa-cha!^*+" not in license_text:
    print("Missing required Wa-cha!^*+ plug in license.")
    sys.exit(1)

readme = (root / "README.md").read_text(encoding="utf-8")
if "completion aid" not in readme.lower():
    print("README should state completion-aid boundary.")
    sys.exit(1)

print("PASS: Wa-cha PromptJects public repo package validates.")
print("RWAL: BINARY_SCORE=1")
