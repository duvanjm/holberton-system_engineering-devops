#!/usr/bin/python3
"""Write a function that queries the Reddit API
and prints the titles of the first 10 hot posts"""

import requests


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts"""
    headers = {"User-Agent": "Holberton"}
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(
                       subreddit)
    req = requests.get(url, headers=headers)

    if req.status_code != 200:
        print(None)
        return
    redit = req.json().get("data").get("children")
    for chil in redit:
        print(chil.get("data").get("title"))
