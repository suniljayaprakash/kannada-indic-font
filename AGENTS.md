# Task Log & State Machine

## Project Status: [🟡 IN PROGRESS]

## Task History

- [x] **Glyph Naming:** Migration from iFontMaker hex names to Glyphs 3 human-readable names (`-kannada` suffix).
- [x] **Class Definition:** Created `@Consonants`, `@Vattus`, and 15 `@[vowel]Ligatures` classes.
- [x] **Feature blwf:** Implemented vattu substitutions and fallback logic for half-letters (standalone ಸ್).
- [x] **Feature akhn:** Expanded to 341 individual substitution rules (34 consonants × 10 vowels + 1 aiMatra) — fixes "Cannot substitute by multiple ligature glyphs".

## Known Configuration

- **Standard Consonant Order:** ka, kha, ga, gha, nga, ca, cha, ja, jha, nya, tta, ttha, dda, ddha, nna, ta, tha, da, dha, na, pa, pha, ba, bha, ma, ya, ra, la, va, sha, ssa, sa, ha, lla, rra, llla.
- **Consonants WITH ligature glyphs (34):** all above except rra and llla (those glyphs are missing).
- **Vowels with full ligature sets (34 each):** aaMatra, iMatra, iiMatra, uMatra, uuMatra, eMatra, eeMatra, oMatra, ooMatra, auMatra.
- **Vowels with partial ligatures:** aiMatra (ka only), vocalicR/RR/L/LL (none — pending).

## Why Individual Rules (not class-based)

Glyphs 3 / AFDKO throws "Cannot substitute by multiple ligature glyphs" when the `by` clause of a GSUB type-4 rule is a glyph class. Each rule must output a single glyph. `lookupflag IgnoreMarks` was also removed because Glyphs 3 assigns matras `category = Mark` (GDEF class 3), which IgnoreMarks would silently skip, preventing the rules from ever firing.

## Next Steps

1. Add `rra` and `llla` ligature glyphs for all vowel types (currently missing).
2. Add remaining `ai`, `vocalicR`, `vocalicRR`, `vocalicL`, `vocalicLL` ligature glyphs and rules.
3. Verify rendering of complex clusters (e.g., ಸ್ಕೋ).
