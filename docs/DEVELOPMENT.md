# Development Guide

This guide covers development setup, dependencies, and workflow for the `github-domain-scraper` project.

## Optional Dependencies

The project defines several optional dependency groups in `pyproject.toml`:

### Build Dependencies
```bash
pip install -e .[build]
```
Includes:
- `build` - For building distribution packages
- `twine` - For uploading packages to PyPI

### Development Dependencies
```bash
pip install -e .[dev]
```
Includes:
- `black` - Code formatting
- `bumpver` - Version bumping
- `isort` - Import sorting
- `mypy` - Type checking
- `pytest` - Testing framework

### All Dependencies
```bash
pip install -e .[build,dev]
```
Installs both build and development dependencies.

## Development Workflow

### 1. Setup Development Environment
```bash
# Clone and setup
git clone https://github.com/Parth971/github-domain-scraper.git
cd github-domain-scraper
pip install -e .[build,dev]
```

### 2. Code Quality Tools

#### Formatting
```bash
# Format code with black
black src/ tests/

# Sort imports
isort src/ tests/
```

#### Type Checking
```bash
# Run type checker
mypy src/
```

#### Testing
```bash
# Run tests
pytest tests/
```

### 3. Making Changes

1. Create a feature branch
2. Make your changes
3. Run code quality tools
4. Test your changes
5. Commit with descriptive messages

### 4. Publishing

See [PUBLISHING.md](./PUBLISHING.md) for the complete publishing process.

## Project Structure

```
github-domain-scraper/
├── src/github_domain_scraper/     # Main package source
│   ├── __init__.py
│   ├── __main__.py
│   ├── backends/                  # Backend implementations
│   ├── driver.py                  # WebDriver management
│   ├── exceptions.py              # Custom exceptions
│   ├── extractor.py               # Main extraction logic
│   └── logger.py                  # Logging configuration
├── tests/                         # Test files
├── examples/                      # Usage examples
├── docs/                          # Documentation
├── pyproject.toml                 # Project configuration
└── README.md                      # Main README
```

## Configuration Files

### pyproject.toml
- Project metadata and dependencies
- Build system configuration
- Tool configurations (black, isort, mypy, etc.)

### .gitignore
- Excludes build artifacts, cache files, and sensitive data

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Ensure all tests pass
5. Submit a pull request

## Testing

The project uses pytest for testing. Tests are located in the `tests/` directory.

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run specific test file
pytest tests/test_user_profile.py
``` 