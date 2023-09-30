"""Usage:
--------

    $ github_domain_scraper --link=<github_link> [--json=filename] [--max-repositories=<max_repositories>]

    where github_link is the URL of GitHub domain
    filename is the json file name. e.g. username.json
    max_repositories is an optional argument to limit the number of repositories to scrape.

Version:
--------

- github-domain-scraper v1.0.2
"""
import argparse
import json

from github_domain_scraper.link_extractor import LinkExtractor
from github_domain_scraper.logger import get_logger

logger = get_logger(__file__)

def parse():
    parser = argparse.ArgumentParser(description="GitHub Domain Scraper")
    parser.add_argument("--link", type=str, help="GitHub link to scrape", required=True)
    parser.add_argument("--json", type=str, help="JSON file to save results")
    parser.add_argument("--max-repositories", type=int, help="Maximum number of repositories to scrape")

    return parser.parse_args()


def extract(link, jsonfile, max_repositories):
    extractor = LinkExtractor(initial_link=link, total_links_to_download=max_repositories)
    result = extractor.extract()

    if jsonfile:
        with open(jsonfile, "w") as file:
            json.dump(result, file, indent=4)
        logger.info(f'Saved links to {jsonfile}')
    else:
        logger.info(f"Extracted domains are {result}")


def main():
    args = parse()
    extract(args.link, args.json, args.max_repositories)


if __name__ == "__main__":
    main()
