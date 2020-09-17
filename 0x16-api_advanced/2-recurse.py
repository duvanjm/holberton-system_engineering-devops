#!/usr/bin/python3
"""recursive function that queries the Reddit API
and returns a list containing the titles of all hot
articles for a given subreddit."""

import requests


def recurse(subreddit, hot_list=[], after=""):
    """returns a list containing the titles of all
    hot articles for a given subreddit"""
    headers = {"User-Agent": "Holberton"}
    url = "https://www.reddit.com/r/{}/hot.json?after={}".format(
                       subreddit, after)
    req = requests.get(url, headers=headers)

    if req.status_code != 200:
        return
    redit = req.json().get("data").get("children")
    for chil in redit:
        hot_list.append(chil.get("data").get("title"))

    after = req.json().get("data").get("after")
    if after is None:
        return hot_list
    else:
        return recurse(subreddit, hot_list, after)
