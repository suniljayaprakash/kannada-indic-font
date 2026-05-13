# Nanni Indic Font

A comprehensive OpenType font project for the Kannada script with advanced typographic features including ligatures, vattus (conjuncts), and matra substitutions.

## Project Overview

This repository contains the source files and tools for building a high-quality Kannada font with proper OpenType shaping support. The project includes:

- **Glyph Design**: Complete Kannada character set with ligatures
- **OpenType Features**: blwf (Below Base Forms), pres (Pre-Base Substitutions), calt (Contextual Alternates)
- **Vattu Support**: Proper rendering of consonant clusters with vattu forms
- **Matra Handling**: Complete vowel sign substitution system

## Directory Structure

```
nanni-indic-font/
├── sources/                    # Source font files
│   ├── Bilvafont-experiments.glyphs   # Primary Glyphs design file
│   └── Nanni-Medium.ufo/       # UFO (Unified Font Object) format
│
├── scripts/                    # Utility scripts
│   ├── add_missing_ligatures.py
│   ├── add_multilevel_vattu.py
│   ├── add_vocalic_pres_rules.py
│   ├── check_classes.py
│   ├── copy_bottom_anchor_ka.py
│   ├── fix_classes.py
│   ├── fix_ligatures.py
│   ├── generate_halant_lookups.py
│   ├── scale_vattu_r.py
│   └── export_ttf.py           # Build TTF with auto-versioning
│
├── builds/                     # Compiled font outputs
│   └── Nanni.ttf              # TrueType font file
│
├── docs/                       # Documentation
│   ├── KANNADA_FONT_CONTEXT.md # Detailed project notes
│   └── AGENTS.md               # Task tracking & development state
│
├── README.md                   # This file
├── CONTRIBUTING.md             # Contribution guidelines
├── LICENSE                     # License
└── .gitignore                  # Git ignore rules
```

## Quick Start

### Prerequisites

- [Glyphs 3](https://glyphsapp.com/) - Font design software
- Python 3.6+
- glyphsLib package: `pip install glyphsLib`

### Building the Font

Export the font with auto-versioning:

```bash
cd nanni-indic-font/scripts
python3 export_ttf.py
```

This script:

- Automatically increments the version number
- Applies remove-overlap and autohinting
- Exports to `builds/` folder with version in filename

### Manual Export in Glyphs

1. Open `sources/Bilvafont-experiments.glyphs`
2. File → Export → TrueType
3. Enable options:
   - Remove Overlap
   - Autohint
   - Use Typographic Naming (if desired)
4. Save to `builds/`

## OpenType Features

### Implemented Features

- **blwf** (Below Base Forms): Vattu substitutions for consonant clusters
- **pres** (Pre-Base Substitutions): Matra ligatures (341 rules for 34 consonants × 10 vowels)
- **calt** (Contextual Alternates): Contextual glyph substitutions

### Feature Notes

- Vattus fire in `blwf` before matra rules in `pres`
- Matra rules skip vattu marks using `lookupflag UseMarkFilteringSet @Matras`
- Individual rules (not class-based) due to AFDKO multi-ligature limitations

## Glyph Classes

Key glyph classes defined in the font:

- `@Consonants` - All 34 Kannada consonants
- `@Vattus` - Vattu forms (bottom and right positioning)
- `@Matras` - Vowel sign marks (15 types)
- `@[vowel]Ligatures` - Ligature sets for each vowel type

See `docs/KANNADA_FONT_CONTEXT.md` for detailed documentation.

## Development

### Running Utility Scripts

```bash
cd nanni-indic-font/scripts

# Check glyph classes
python3 check_classes.py

# Fix ligature issues
python3 fix_ligatures.py

# Add vocalic matras
python3 add_vocalic_pres_rules.py
```

### Project Status

Current focus areas:

- ✅ Core Kannada consonants and vowels
- ✅ Vattu support (multi-level clusters)
- ✅ Matra substitutions
- 🔄 Additional ligature sets (rra, llla)
- 🔄 Vocalic matra ligatures (vocalicR, vocalicRR, vocalicL, vocalicLL)

See `docs/AGENTS.md` for detailed task tracking.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on:

- Reporting issues
- Submitting contributions
- Development workflow
- Code style conventions

## License

This project is licensed under the [LICENSE](LICENSE) file.

## Contact & Support

For questions or issues, please open a GitHub issue or discussion.

## Resources

- [Unicode Kannada Characters](https://en.wikipedia.org/wiki/Kannada_script)
- [Unicode Kannada Block (U+0C80–U+0CFF)](https://unicode.org/charts/PDF/U0C80.pdf)
- [Unicode Vedic Extensions (U+1CD0–U+1CF9)](https://unicode.org/charts/PDF/U1CD0.pdf)
- [OpenType Specification](https://docs.microsoft.com/en-us/typography/opentype/)
- [Glyphs 3 Documentation](https://glyphsapp.com/learn)
- [glyphsLib Documentation](https://glyphslib.readthedocs.io/)
