# Quick Publishing Reference

## One-Liner Publishing (for experienced users)

```bash
git add . && git commit -m "feat: your change description" && bumpver update --minor && git push origin main --tags && python -m build && twine check dist/* && twine upload dist/*
```

## Step-by-Step Commands

```bash
# 1. Commit changes
git add .
git commit -m "feat: your change description"

# 2. Bump version
bumpver update --minor  # or --patch or --major

# 3. Push to GitHub
git push origin main --tags

# 4. Build and publish
python -m build
twine check dist/*
twine upload dist/*
```

## Version Bump Types

- `--patch`: Bug fixes (1.0.0 → 1.0.1)
- `--minor`: New features (1.0.0 → 1.1.0) 
- `--major`: Breaking changes (1.0.0 → 2.0.0)

## Prerequisites

```bash
# Install all publishing dependencies
pip install -e .[build,dev]
```

## Files Updated by bumpver

- `pyproject.toml` (version and current_version)
- `src/github_domain_scraper/__init__.py` (version)
- `src/github_domain_scraper/__main__.py` (version in help)
- Git commit and tag (automatically created) 