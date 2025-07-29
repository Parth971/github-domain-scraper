import json
import os
from typing import Any, Dict, Set
from github_domain_scraper.extractor import UserProfileInformationExtractor
import pandas as pd


def get_usernames() -> Set[str]:
    with open("out/stargazer_profiles.json", "r") as file:
        stargazer_profiles = json.load(file)
    usernames = [
        stargazer_profile["username"] for stargazer_profile in stargazer_profiles
    ]
    return set(usernames)


def filter_usernames(usernames: Set[str], jsonfile: str) -> Set[str]:
    already_extracted_usernames = set()
    if os.path.exists(jsonfile):
        with open(jsonfile, "r") as file:
            existing_result = json.load(file)
        already_extracted_usernames = set(existing_result.keys())
    return usernames - already_extracted_usernames


def create_or_update_json(jsonfile: str, result: Dict[str, Any]) -> None:
    if os.path.exists(jsonfile):
        with open(jsonfile, "r") as file:
            existing_result = json.load(file)
        result = {**existing_result, **result}

    with open(jsonfile, "w") as file:
        json.dump(result, file, indent=4)


def convert_to_csv(jsonfile: str, csvfile: str) -> None:
    with open(jsonfile, "r") as file:
        data = json.load(file)
    df = pd.DataFrame(data.values())
    df.to_csv(csvfile, index=False)


if __name__ == "__main__":
    jsonfile = "out/user_profiles.json"
    csvfile = "out/user_profiles.csv"
    batch = 100
    raw_usernames = get_usernames()

    print(f"Found {len(raw_usernames)} usernames.")

    filtered_usernames = filter_usernames(raw_usernames, jsonfile)

    print(f"Found {len(filtered_usernames)} usernames after filtering.")

    usernames = list(filtered_usernames)

    print(f"Extracting {len(usernames)} usernames.")

    for i in range(0, len(usernames), batch):
        batch_usernames = usernames[i : i + batch]  # noqa: E203

        print(f"\nExtracting batch {i} to {i + batch}")

        extractor = UserProfileInformationExtractor(
            github_username=batch_usernames,
            headless=True,
            login_first=True,
            login_username="XXX",
            login_password="XXX",
        )
        extracted_result = extractor.extract()

        result = {
            username: user_profile.to_dict(flatten=True)
            for username, user_profile in extracted_result.items()
        }

        create_or_update_json(jsonfile, result)

        print(f"Saved {len(result)} user's information to {jsonfile}")

    print(f"Saved user's information to {jsonfile}")

    convert_to_csv(jsonfile, csvfile)

    print(f"Saved user's information to {csvfile}")
