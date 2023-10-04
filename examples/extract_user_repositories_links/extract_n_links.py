# Import the LinkExtractor class from the github_domain_scraper package
from github_domain_scraper.extractor import LinkExtractor

if __name__ == '__main__':
    # Define the GitHub user's profile link
    link = "https://github.com/Parth971"

    # Define the number of links from the user's repository to extract
    n = 10

    # Create an instance of the LinkExtractor class with the initial link and desired link count
    extractor = LinkExtractor(initial_link=link, total_links_to_download=n)

    # Extract the specified number of links from the user's repository
    links = extractor.extract()

    # Print the extracted links
    print(links)
