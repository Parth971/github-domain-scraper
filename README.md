# github-domain-scraper

## Installation

You can install the `github-domain-scraper` from [PyPI](https://pypi.org/project/realpython-reader/):

    python -m pip install github-domain-scraper

The reader is supported on Python 3.8 and above.

## How to use

The `github-domain-scraper` is having wide variety of use-cases

1. Command-line tool: It can be used as command-line tool

   ```
   python -m github_domain_scraper --link=https://github.com/Parth971
   ```
   ```
   python -m github_domain_scraper --link=https://github.com/Parth971 --json=repo.json
   ```

2. It can also be used inside other python modules as well

   ```python
   from github_domain_scraper.link_extractor import LinkExtractor
   
   links = LinkExtractor(initial_link="github_link").extract()
   ```
