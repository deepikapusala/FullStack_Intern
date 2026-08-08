# Specificity Worksheet — Send Message Button

## Rules Targeting `<button class="send-btn" type="submit">`

| # | Selector | ID Score | Class/Attr Score | Element Score | Total | Result |
|---|---|---|---|---|---|---|
| 1 | `button` | 0 | 0 | 1 | 1 | Lost |
| 2 | `.send-btn` | 0 | 10 | 0 | 10 | Lost |
| 3 | `#contact button` | 100 | 0 | 1 | 101 | Lost |
| 4 | `section button` | 0 | 0 | 2 | 2 | Lost |
| 5 | `form fieldset button` | 0 | 0 | 3 | 3 | Lost |
| 6 | `#contact .send-btn` | 100 | 10 | 0 | 110 | **WON** |
| 7 | `button[type="submit"]` | 0 | 10 | 1 | 11 | Lost |
| 8 | `fieldset button` | 0 | 0 | 2 | 2 | Lost |

## Prediction
Based on manual calculation, `#contact .send-btn` (110 points) should win,
since it combines an ID selector (100) with a class selector (10) —
higher than any other rule in the list.

## Verification (DevTools)
Confirmed in Chrome DevTools → Elements → Styles panel. The button rendered
**red**, matching `#contact .send-btn`. This rule appeared at the top of the
Styles panel, not struck through, while all other rules were shown with
strikethrough — confirming the manual calculation was correct.

See: screenshots/devtools-specificity.png

## Key Takeaway
Specificity is NOT about which rule is written last in the file — it's
about scoring each selector (ID=100, Class/attribute=10, Element=1) and
adding them up. The highest score wins, regardless of source order.