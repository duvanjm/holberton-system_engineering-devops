#!/usr/bin/python3
"""Write a function that queries the Reddit API
and returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers"""
    headers = {"User-Agent": "Holberton"}

    req = requests.get("https://www.reddit.com/r/{}/about.json".format(
                       subreddit), headers=headers).json()
    if req.get("data").get("subscribers"):
        return req.get("data").get("subscribers")
    else:
        return 0
