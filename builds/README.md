# Compiled Font Builds

This directory contains exported font files (TTF, OTF, WOFF, etc.) ready for distribution or testing.

## Latest Build

- **Nanni.ttf** - Latest compiled TrueType font

## Version History

Each exported font includes version number in the filename:

- `Nanni-v1.6.ttf`
- `Nanni-v1.7.ttf`
- etc.

## Building

To generate a new build with auto-versioning:

```bash
cd scripts
python3 export_ttf.py
```

This will:

1. Increment the version number in the source file
2. Export TTF with remove-overlap and autohinting enabled
3. Save to this directory with version in the filename

## Installation

### macOS

1. Double-click the TTF file
2. Click "Install Font" in Font Book

### Windows

1. Right-click the TTF file
2. Select "Install" or "Install for all users"

### Linux

```bash
mkdir -p ~/.fonts
cp *.ttf ~/.fonts/
fc-cache -f -v
```

## Testing

Test fonts using:

- Font Book (macOS)
- Character Map (Windows)
- Design apps (Figma, Adobe Creative Suite)
- Web browsers (WOFF format when available)
