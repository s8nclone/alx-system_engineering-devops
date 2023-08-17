#!/usr/bin/python3
"""Function that queries the Reddit API and
returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """returns number of subscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    resp = requests.get(url, headers=headers, allow_redirects=False)
    if resp.status_code == 404:
        return 0
    results = resp.json().get("data")
    return results.get("subscribers")
