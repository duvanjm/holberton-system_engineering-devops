#!/usr/bin/python3
"""Write a Python script that, using this
REST API, for a given employee ID, returns
information about his/her TODO list progress."""

import requests
import sys
import json


if __name__ == "__main__":

    def _request(val, task):
        """reques for user"""
        url = 'https://jsonplaceholder.typicode.com'
        info = "{}{}{}".format(url, val, task)
        return requests.get(info).json

    def user_(task):
        """request for user"""
        user = _request("/users/", task)
        todo = _request("/todos/?userId=", task)
        done = [i.get("title") for i in todo if i.get("complete")]
        all = len(todo)
        print('Employee {} is done with tasks({}/{}):'.format(
            user.get('name'), len(done), all))
        for i in done:
            print("\t {}".format(t))
