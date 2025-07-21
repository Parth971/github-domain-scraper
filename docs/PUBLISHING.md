# Publishing Guide

This document outlines the complete process for publishing new versions of the `github-domain-scraper` package to PyPI.

## Prerequisites

Before publishing, ensure you have the following tools installed:

### Option 1: Install individual packages
```bash
pip install bumpver build twine
```

### Option 2: Install using project's optional dependencies
```bash
# Install build dependencies (includes build and twine)
pip install -e .[build]

# Install development dependencies (includes bumpver and other dev tools)
pip install -e .[dev]

# Or install both
pip install -e .[build,dev]
```

### Option 3: Install all dependencies at once
```bash
# Install all optional dependencies
pip install -e .[build,dev]
```

## Publishing Process

### 1. Commit Your Changes

First, commit all your changes to git:

```bash
# Add your modified files
git add <modified_files>

# Commit with a descriptive message
git commit -m "feat: Add new user profile properties (uid, projects, contribs, contrib_matrix, type, url) and improve type safety"
```

### 2. Bump Version Number

Use `bumpver` to automatically update the version number in all relevant files:

```bash
# For minor version bump (new features)
bumpver update --minor

# For patch version bump (bug fixes)
bumpver update --patch

# For major version bump (breaking changes)
bumpver update --major
```

This will:
- Update version in `pyproject.toml`
- Update version in `src/github_domain_scraper/__init__.py`
- Update version in `src/github_domain_scraper/__main__.py`
- Create a git commit with the version bump
- Create a git tag for the new version

### 3. Push to GitHub

Push your changes and tags to GitHub:

```bash
git push origin main --tags
```

### 4. Build Distribution

Build both wheel and source distributions:

```bash
python -m build
```

This creates:
- `dist/github_domain_scraper-<version>-py3-none-any.whl` (wheel distribution)
- `dist/github_domain_scraper-<version>.tar.gz` (source distribution)

### 5. Verify Distributions

Check that the distribution files are valid:

```bash
twine check dist/*
```

Both files should show "PASSED" status.

### 6. Upload to PyPI

Upload the distributions to PyPI:

```bash
twine upload dist/*
```

You'll be prompted for your PyPI username and password (or API token).

## Version Numbering

Follow [Semantic Versioning](https://semver.org/) (MAJOR.MINOR.PATCH):

- **MAJOR**: Breaking changes that require users to update their code
- **MINOR**: New features added in a backward-compatible manner
- **PATCH**: Bug fixes in a backward-compatible manner

## Configuration Files

### pyproject.toml

The main configuration file contains:

```toml
[project]
name = "github-domain-scraper"
version = "3.1.0"  # Updated by bumpver
description = "..."
# ... other project metadata

[tool.bumpver]
current_version = "3.1.0"
version_pattern = "MAJOR.MINOR.PATCH"
commit_message  = "bump version {old_version} -> {new_version}"
commit          = true
tag             = true
push            = false

[tool.bumpver.file_patterns]
"pyproject.toml" = [
    'current_version = "{version}"',
    'version = "{version}"',
]
"src/github_domain_scraper/__init__.py" = ["{version}"]
"src/github_domain_scraper/__main__.py" = ["- github-domain-scraper v{version}"]
```

## What Gets Updated

When you run `bumpver update`, it automatically updates:

1. **pyproject.toml**: Both `version` and `current_version` fields
2. **src/github_domain_scraper/__init__.py**: Version string
3. **src/github_domain_scraper/__main__.py**: Version in help text
4. **Git**: Creates commit and tag

## Complete Example

Here's a complete example of publishing a new version:

```bash
# 1. Make your changes and commit them
git add .
git commit -m "feat: Add new feature X"

# 2. Bump version (minor for new features)
bumpver update --minor

# 3. Push to GitHub
git push origin main --tags

# 4. Build distributions
python -m build

# 5. Check distributions
twine check dist/*

# 6. Upload to PyPI
twine upload dist/*
```

## Troubleshooting

### Build Warnings

You may see deprecation warnings about license format:
```
SetuptoolsDeprecationWarning: `project.license` as a TOML table is deprecated
```

These are warnings and don't prevent the build from succeeding. To fix them, update the license format in `pyproject.toml`:

```toml
# Old format (deprecated)
license = { file = "LICENSE" }

# New format (recommended)
license = "MIT"
license-files = { paths = ["LICENSE"] }
```

### Authentication Issues

If you have trouble with PyPI authentication:

1. Use an API token instead of password
2. Store credentials using `keyring`:
   ```bash
   keyring set https://upload.pypi.org/legacy/ your-username
   ```

## Post-Publishing

After successful upload:

1. **Verify on PyPI**: Check https://pypi.org/project/github-domain-scraper/
2. **Test Installation**: Try installing the new version:
   ```bash
   pip install github-domain-scraper==<new_version>
   ```
3. **Update Documentation**: If needed, update README.md or other docs

## Release Notes

For each release, consider creating release notes that document:

- New features added
- Bug fixes
- Breaking changes
- Migration guide (if needed)

This helps users understand what's changed and how it affects their code. 