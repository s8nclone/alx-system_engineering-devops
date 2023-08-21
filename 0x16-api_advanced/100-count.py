#!/usr/bin/python3
"""
Function that queries the Reddit API, parses the title of all
Hot articles and prints a sorted count of given keywords.
"""
import requests


def count_words(subreddit, word_list, instances={}, after="", count=0):
    """Prints sorted counts of given keywords found in hot articles.

    Args:
        subreddit (str): The subreddit to search.
        word_list (list): The list of words to search for in post titles.
        instances (obj): Key/value pairs of words/counts.
        after (str): The parameter for the next page of the API results.
        count (int): The parameter of results matched thus far.
    """
    link = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    resp = requests.get(link, headers=headers, params=params,
                        allow_redirects=False)
    try:
        res = resp.json()
        if resp.status_code == 404:
            raise Exception
    except Exception:
        print("")
        return

    res = res.get("data")
    after = res.get("after")
    count += res.get("dist")
    for x in res.get("children"):
        title = x.get("data").get("title").lower().split()
        for word in word_list:
            if word.lower() in title:
                times = len([t for t in title if t == word.lower()])
                if instances.get(word) is None:
                    instances[word] = times
                else:
                    instances[word] += times

    if after is None:
        if len(instances) == 0:
            print("")
            return
        instances = sorted(instances.items(), key=lambda kv: (-kv[1], kv[0]))
        [print("{}: {}".format(k, v)) for k, v in instances]
    else:
        count_words(subreddit, word_list, instances, after, count)
