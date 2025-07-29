import json
import os
from typing import Any, Dict, List
from github_domain_scraper.extractor import StargazerProfilesExtractor


def create_or_update_json(jsonfile: str, result: List[Dict[str, Any]]) -> None:
    if os.path.exists(jsonfile):
        with open(jsonfile, "r") as file:
            existing_result = json.load(file)
        result = existing_result + result

    with open(jsonfile, "w") as file:
        json.dump(result, file, indent=4)


if __name__ == "__main__":
    jsonfile = "out/stargazer_profiles.json"
    initial_link = "https://github.com/voideditor/void/stargazers"

    extractor = StargazerProfilesExtractor(
        initial_link=initial_link,
        headless=False,
        login_first=False,
    )

    for page in range(1, 100, 10):
        start_page = page
        end_page = page + 9

        print(f"Extracting page {start_page} to {end_page}")

        extracted_result = extractor.extract(start_page=start_page, end_page=end_page)

        result = [
            stargazer_profile.to_dict()
            for stargazer_profiles in extracted_result.values()
            for stargazer_profile in stargazer_profiles
        ]

        create_or_update_json(jsonfile, result)

    print(f"Saved stargazer profiles to {jsonfile}")
