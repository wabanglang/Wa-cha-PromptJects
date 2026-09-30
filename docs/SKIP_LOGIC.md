# Skip Logic

Use skip logic to reduce burden without hiding required facts.

## Core pattern

```text
IF answer = Yes:
    collect required follow-up fields.
IF answer = No:
    skip the dependent section.
IF answer = Unknown:
    flag for advocate review.
```

## Examples

| Trigger | If No | If Yes |
|---|---|---|
| Has income? | Skip employer, wages, pay frequency, paystubs | Collect income source, amount, frequency, proof |
| Has vehicle? | Skip make/model/year/value/loan | Collect vehicle details |
| Has dependents? | Skip child/dependent sections | Collect dependent details |
| Has bank account? | Skip bank name/account/balance | Collect account type and balance |
| Has fixed address? | Use homeless/no fixed address workflow | Collect residential address |
| Has phone? | Do not select text/call as contact method | Collect phone and consent choices |
| Has authorized representative? | Skip representative fields | Collect representative name/contact/signature if required |
| Applies for health coverage too? | Skip health-only fields | Complete health coverage fields |

## Rule

Skipping is valid only when the field is truly not applicable or not triggered by the profile. Do not skip required fields to conceal relevant facts.
