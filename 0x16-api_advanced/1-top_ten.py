#!/usr/bin/python3
"""1-top_ten

Run ./1-main.py programming or ./1-main.py this_is_a_fake_subreddit for testing
"""

import requests


def top_ten(subreddit):
    """Function that queries the Reddit API and prints the titles of the
    first 10 hot posts listed for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "1-top_ten.py"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200 and response.text.strip():
        for post in response.json().get("data").get("children"):
            print(post.get("data").get("title"))
    else:
        print(None)
