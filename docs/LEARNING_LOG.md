# Learning log

Record observable changes, not just viewing time. Entries may be written in English or Chinese; do not invent past reflections.

## 2026-11-07 · Repository organization

- User-reported course progress: a little over four hours. Uploaded evidence: ten Python scripts.
- Grouped scripts by topic and retained the original Git history. The course index maps old names to new locations.
- Kept both single-item and multi-item shopping carts.
- With AI assistance: allowed a 12-character alphabetic username as the existing comment specifies; fixed the quiz option to William Shakespeare; changed the guessing counter to count valid in-range guesses; enforced its stated 1–100 range; adjusted a nested f-string for Python 3.10 compatibility.
- Validation: Python 3.13.15 locally; all 10 scripts compiled and 6 focused regression checks passed. Python 3.10 grammar compatibility was also checked; no full Python 3.10 runtime run is claimed.
- Added focused regression checks. This entry records maintenance, not a learner reflection or proof of independent implementation.

## Next improvements

- [ ] After learning functions, extract one calculation from the CLI and test it directly.
- [ ] Handle invalid numeric input and reject negative cart prices/quantities.
- [ ] State and test rules for username punctuation and whitespace.
- [ ] Add a reproducible sample session for one completed improvement.
- [ ] Write a short explanation of a bug personally investigated, including input, cause and fix.

## Template for the next real session

Copy this block and replace the placeholders only after doing the work:

```markdown
## YYYY-MM-DD · Topic
- Code: [filename](../course/REPLACE_WITH_REAL_PATH.py)
- Source: course chapter / documentation link / independent design.
- What I implemented:
- One issue I investigated (input → expected → actual → cause → fix):
- Verification I actually ran:
- Help used (tutorial, AI, other):
- Next step:
```
