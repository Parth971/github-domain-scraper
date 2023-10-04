# Import the LinkExtractor class from the github_domain_scraper package
from github_domain_scraper.extractor import LinkExtractor

if __name__ == '__main__':
    # Define the GitHub search link
    link = "https://github.com/search?q=ori+python&type=users"

    # Create an instance of the LinkExtractor class with the initial search link and desired link count
    extractor = LinkExtractor(initial_link=link)

    # To provide max-repositories argument
    # extractor = LinkExtractor(initial_link=link, total_links_to_download=10)

    # Extract links from the search results
    links = extractor.extract()

    # Print the extracted links
    print(links)
