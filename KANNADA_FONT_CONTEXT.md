# Project Context: Kannada Handwriting Font (Digital Preservation)

## Technical Stack

- **Editor:** Glyphs 3
- **Script:** Kannada (Indic)
- **Shaper Tags:** `knda`, `knd2`
- **Naming Suffix:** `-kannada`

## Architectural Rules

1. **The 36-Consonant Matrix:** All consonant-based classes (@Consonants, @Vattus, @[vowel]Ligatures) must contain exactly 36 glyphs in the established standard order (Ka to Llla).
2. **Feature Order:** - `blwf` (Below-base forms): Vattus first, standalone half-forms (e.g., sa_halant) last as a fallback.
   - `akhn` (Akhand): Class-based vowel ligatures.
3. **The Symmetry Rule (CRITICAL):** OpenType compilers require 1-to-1-to-1 symmetry for class substitutions. To swap @Consonants with @aaLigatures, a "Trigger Class" (@aaMatraClass) containing the matra name repeated 36 times is required.
4. **Shaping Fixes:**
   - Use `lookupflag IgnoreMarks;` in `akhn` lookups to allow vowels to skip over Vattus (marks).
   - Category for Vattus: `Mark / Nonspacing`.
   - Category for Ligatures: `Letter / Other`.

## Glyph Naming Convention

- Base: `ka-kannada`
- Matra: `aaMatra-kannada` (Mark)
- Ligature: `ka_aaMatra-kannada` (Pre-composed)
- Vattu: `kavattu-kannada` (Mark)
