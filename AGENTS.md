# Task Log & State Machine

## Project Status: [🟡 IN PROGRESS]

## Task History

- [x] **Glyph Naming:** Migration from iFontMaker hex names to Glyphs 3 human-readable names (`-kannada` suffix).
- [x] **Class Definition:** Created `@Consonants`, `@Vattus`, and 15 `@[vowel]Ligatures` classes.
- [x] **Feature blwf:** Implemented vattu substitutions and fallback logic for half-letters (standalone ಸ್).
- [x] **Feature akhn:** Now empty (just a shell lookup). Matra rules moved to `pres`.
- [x] **Feature pres:** 341 individual substitution rules (34 consonants × 10 vowels + 1 aiMatra), `lookupflag UseMarkFilteringSet @Matras`. Fires after `blwf` so vattus are already formed and skipped correctly.
- [x] **Archaic Support:** Added naming and class logic for Vocalic L (ೢ) and Vocalic LL (ೣ) matras.
- [ ] **Symmetry Check:** Ensuring `vocLMatraClass` and `vocLLMatraClass` contain exactly 36 entries to match `@Consonants`.

## Known Configuration

- **Standard Consonant Order:** ka, kha, ga, gha, nga, ca, cha, ja, jha, nya, tta, ttha, dda, ddha, nna, ta, tha, da, dha, na, pa, pha, ba, bha, ma, ya, ra, la, va, sha, ssa, sa, ha, lla, rra, llla.
- **Consonants WITH ligature glyphs (34):** all above except rra and llla (those glyphs are missing).
- **Vowels with full ligature sets (34 each):** aaMatra, iMatra, iiMatra, uMatra, uuMatra, eMatra, eeMatra, oMatra, ooMatra, auMatra.
- **Vowels with partial ligatures:** aiMatra (ka only), vocalicR/RR/L/LL (none — pending).

## Shaping Pipeline Notes

- `akhn` fires BEFORE `blwf`. Matra rules in `akhn` would consume the 2nd consonant before `blwf` can form its vattu — breaking clusters like ಕ್ಕೂ.
- `pres` fires AFTER `blwf`. Vattus are already formed as marks. `lookupflag UseMarkFilteringSet @Matras` skips vattu marks while keeping matras visible (even if matras are GDEF marks).
- Individual rules (not class-based) because Glyphs 3 / AFDKO throws "Cannot substitute by multiple ligature glyphs" when `by` clause is a class.
- `@Matras` class in sidebar = all 15 standalone matra glyphs (used only for the UseMarkFilteringSet filter).

## Next Steps

1. Add `rra` and `llla` ligature glyphs for all vowel types (currently missing).
2. Add remaining `ai`, `vocalicR`, `vocalicRR`, `vocalicL`, `vocalicLL` ligature glyphs and rules.
3. Verify rendering of complex clusters (e.g., ಸ್ಕೋ).
