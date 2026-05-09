# Contributing to Kannada Indic Font

Thank you for your interest in contributing! This document provides guidelines for contributing to the project.

## Getting Started

1. **Fork** the repository on GitHub
2. **Clone** your fork locally:
   ```bash
   git clone https://github.com/YOUR-USERNAME/kannada-indic-font.git
   cd kannada-indic-font
   ```
3. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

## Setting Up Development Environment

### Requirements

- Glyphs 3 (for font editing)
- Python 3.6+
- Git

### Installation

```bash
# Clone the repo
git clone https://github.com/yourusername/kannada-indic-font.git
cd kannada-indic-font

# Create Python virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt  # if available, or:
pip install glyphsLib fonttools
```

## Reporting Issues

### Bug Reports

Include in your issue:

- Clear description of the problem
- Steps to reproduce
- Expected vs. actual behavior
- Screenshots (if applicable)
- Font file version (check AGENTS.md)

### Feature Requests

- Describe the feature and its benefit
- Provide examples if possible
- Link to related Unicode or OpenType standards

## Making Changes

### Workflow

1. **Make your changes** in a feature branch
2. **Test thoroughly**:
   - Verify font renders correctly in Glyphs
   - Test exported TTF in multiple applications
   - Run any relevant Python utility scripts
3. **Document changes**:
   - Update `docs/AGENTS.md` with completed tasks
   - Add comments to complex code
4. **Commit with clear messages**:
   ```bash
   git commit -m "feat: add vocalicR ligatures for all consonants"
   ```

### Code Standards

#### Python Scripts

- Follow PEP 8 style guide
- Add docstrings to functions
- Include comments for complex logic
- Use meaningful variable names

Example:

```python
def increment_version(glyphs_file_path):
    """
    Increment the font version in the Glyphs file.

    Args:
        glyphs_file_path: Path to the .glyphs file

    Returns:
        tuple: (old_version, new_version)
    """
    # Implementation here
    pass
```

#### Font Design

- Use consistent glyph naming conventions (suffix: `-kannada`)
- Document class definitions in `docs/KANNADA_FONT_CONTEXT.md`
- Maintain anchor positioning for proper matra alignment
- Test vattu substitution in complex clusters

### Commit Messages

Use conventional commits format:

```
type(scope): description

[optional body]
[optional footer]
```

**Types**: `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `chore`

**Examples**:

```
feat(glyphs): add rra_aaMatra ligature for all consonants
fix(pres): correct matra positioning for vocalic R matras
docs(context): update feature pipeline notes
```

## Submitting Changes

1. **Push to your fork**:

   ```bash
   git push origin feature/your-feature-name
   ```

2. **Create a Pull Request** on GitHub:
   - Clear title describing the changes
   - Reference related issues: "Fixes #123"
   - Include test results/screenshots
   - Link to relevant documentation

### PR Guidelines

- Keep PRs focused on a single feature or fix
- Include descriptive commit history
- Update `docs/AGENTS.md` if completing tracked tasks
- Respond to review feedback promptly

## Testing

### Font Testing

1. **In Glyphs**:
   - Preview all modified glyphs
   - Test contextual substitutions
   - Check anchor positioning

2. **After export**:
   - Open TTF in font viewer (macOS: Font Book)
   - Test in design apps (Figma, Adobe suite)
   - Verify complex scripts render correctly

### Test Cases for Kannada

Common test strings:

```
ಕ್ಕೂ     # ka + vattu_ka + uuMatra
ಸ್ಕೋ     # sa + vattu_ka + oMatra
ನ್ನೆ     # na + vattu_na + eMatra
```

## Documentation

Updates to documentation are highly valued:

- **KANNADA_FONT_CONTEXT.md**: Technical font architecture
- **AGENTS.md**: Development progress and task tracking
- **README.md**: User-facing project overview

Please keep documentation accurate and up-to-date with code changes.

## Development Tips

### Working with Python Scripts

```bash
# Run a utility script
cd scripts
python3 check_classes.py

# Debug output
python3 -u script_name.py  # Unbuffered output
```

### Git Tips

```bash
# View changes before committing
git diff

# Undo recent changes
git checkout -- filename

# Squash commits
git rebase -i HEAD~3

# View commit history
git log --oneline -n 10
```

## Code Review

All submissions require review. Maintainers will:

- Review for correctness
- Check consistency with project goals
- Suggest improvements if needed
- Approve and merge when ready

Please be patient during review and respond to feedback constructively.

## License

By contributing, you agree that your contributions will be licensed under the same license as the project (see LICENSE file).

## Questions?

- Open a GitHub Discussion
- Create an issue for clarification
- Review existing documentation first

Thank you for contributing! 🎉
