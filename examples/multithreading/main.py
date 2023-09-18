from threading import Thread
from github_domain_scraper.link_extractor import LinkExtractor


# Define a function to perform extraction in a thread
def extractor(link, filename):
    LinkExtractor(initial_link=link).extract(jsonfile=filename)


if __name__ == '__main__':
    # Define a list of input tuples, each containing a URL and a corresponding JSON filename
    inputs = (
        ("https://github.com/Parth971", "Parth971.json"),
        ("https://github.com/mavine4512?tab=repositories", "mavine4512.json"),
        ("https://github.com/mavinothkumar/", "mavinothkumar.json"),
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
