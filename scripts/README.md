# Utility Scripts for Kannada Font

This directory contains Python utility scripts for managing and building the Kannada font.

## Available Scripts

### Building & Export

- **export_ttf.py** - Export TTF with auto-versioning (increments version on each run)

### Glyph Management

- **add_missing_ligatures.py** - Add missing ligature glyphs
- **fix_ligatures.py** - Fix and repair ligature definitions
- **add_multilevel_vattu.py** - Add multi-level vattu (consonant cluster) support

### Feature Engineering

- **add_vocalic_pres_rules.py** - Add matra substitution rules
- **generate_halant_lookups.py** - Generate halant-based lookups

### Validation & Maintenance

- **check_classes.py** - Validate glyph class definitions
- **fix_classes.py** - Fix class inconsistencies
- **copy_bottom_anchor_ka.py** - Copy anchor positions for standardization
- **scale_vattu_r.py** - Scale right-positioned vattus

## Usage

```bash
# Run a script
cd scripts
python3 script_name.py

# Most scripts read from the source Glyphs file and may modify it
# Always backup before running!
```

## Prerequisites

```bash
pip install glyphsLib fonttools
```

## Notes

- Scripts operate on the font file(s) in `sources/`
- Always commit or backup your font before running scripts
- Check script docstrings for specific usage and parameters

See the main README.md for more information.
