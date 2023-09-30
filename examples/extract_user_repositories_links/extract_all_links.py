# Import the LinkExtractor class from the github_domain_scraper package
from github_domain_scraper.link_extractor import LinkExtractor

if __name__ == '__main__':
    # Define the GitHub user's profile link
    link = "https://github.com/Parth971"

    # Create an instance of the LinkExtractor class with the initial link
    extractor = LinkExtractor(initial_link=link)

    # Extract links from the user's repository
    links = extractor.extract()

    # Print the extracted links
    print(links)
