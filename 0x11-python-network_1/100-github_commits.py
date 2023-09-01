#!/usr/bin/python3
"""
10. Time for an interview!
"""

import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <repository_name> <owner_name>")
        sys.exit(1)

    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"

    try:
        req = requests.get(url)

        if req.status_code == 200:
            data = req.json()

            for commit in data[:10]:
                sha_code = commit['sha']
                author_name = commit['commit']['author']['name']
                print(f"{sha_code}: {author_name}")
            else:
                print("Error: Unable to fetch commits")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)
