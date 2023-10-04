# Import the LinkExtractor class from the github_domain_scraper package
from github_domain_scraper.extractor import LinkExtractor

if __name__ == '__main__':
    # Define the GitHub search link
    link = "https://github.com/search?q=ori+python&type=users"

    # Define the number of links to extract
    n = 10

    # Create an instance of the LinkExtractor class with the initial search link and desired link count
    extractor = LinkExtractor(initial_link=link, total_links_to_download=n)

    # Extract links from the search results
    links = extractor.extract()

    # Print the extracted links
    print(links)
