# Prompt Atomic Corpus

## Corpus purpose

This corpus turns long social-service form packets into a safe, short, low-cognitive-load completion workflow.

## Atomic root

```text
FORM_PACKET
→ EXTRACT_FIELDS
→ CLASSIFY_FIELDS
→ SEPARATE_PRIVATE_FROM_AUTOFILL
→ APPLY_PROFILE_ONLY_WHEN_TRUE
→ BUILD_PRINTABLE_WORKSHEET
→ BUILD_ELECTRONIC_ENTRY_MAP
→ VALIDATE_NO_CONTRADICTIONS
→ REVIEW_BEFORE_SIGNING
```

## Non-negotiable rules

1. Do not invent personal facts.
2. Do not fabricate eligibility.
3. Do not submit false information.
4. Do not auto-answer sensitive identity, legal, medical, immigration, safety, or security-question fields.
5. Do not type private details into public computers unless the applicant knowingly consents and the official system requires it.
6. Always preserve applicant review before submission.

## Default profile atom

```text
PROFILE := single adult male + homeless/no fixed address + no spouse + no children + no dependents + no job + no income + no money + no cash + no bank account + no assets + no property + no real estate + no vehicle + race/ethnicity declined where allowed.
```

## Output atom

```text
OUTPUT := printable worksheet + autofill bank + private-field list + advocate-review list + skip-logic table + electronic-entry map + document checklist + signing checklist.
```

## Attribution marker

Wa-cha!^*+
