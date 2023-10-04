import json
from threading import Thread
from github_domain_scraper.extractor import LinkExtractor


# Define a function to perform extraction in a thread
def extractor(link, filename):
    links = LinkExtractor(initial_link=link).extract()
    print(links)

    # here you can implement other functionality after getting list of search result links
    with open(filename, "w") as file:
        json.dump(links, file, indent=4)

    print(f'Saved links to {filename}')


if __name__ == '__main__':
    # Define a list of input tuples, each containing a URL and a corresponding JSON filename
    inputs = (
        ("https://github.com/search?q=ori+python&type=users", "users.json"),
        ("https://github.com/search?q=Python+&type=marketplace", "marketplaces.json"),
        ("https://github.com/search?q=created%3A%3E2023-10-02&type=topics&ref=advsearch", "topics.json"),
    )

    threads = []

    # Create and start a thread for each input
    for url, json_file_name in inputs:
        thread = Thread(target=extractor, args=(url, json_file_name))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    print("All threads have completed")
