#!/usr/bin/python3
"""Write a Python script that, using this
REST API, for a given employee ID, returns
information about his/her TODO list progress."""

import requests
import sys
import csv


def _request(val, task):
    """reques for user"""
    url = 'https://jsonplaceholder.typicode.com'
    info = '{}{}{}'.format(url, val, task)
    return requests.get(info).json()


def user_(task):
    """reques for user"""
    user = _request('/users/', task)
    todo = _request('/todos/?userId=', task)
    user_name = user.get('username')
    done = [[t.get('completed'), t.get('title')] for t in todo]
    file = task + '.csv'
    with open(file, 'w') as csvfile:
        spamwriter = csv.writer(
            csvfile, delimiter=',', quoting=csv.QUOTE_ALL
        )
        for all in done:
            spamwriter.writerow([task, user_name, all[0], all[1]])


if __name__ == '__main__':
    """main"""
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        user_(sys.argv[1])
