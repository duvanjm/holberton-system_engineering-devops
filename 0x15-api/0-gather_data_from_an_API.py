#!/usr/bin/python3
"""Write a Python script that, using this
REST API, for a given employee ID, returns
information about his/her TODO list progress."""

import requests
import sys
import json


def _request(val, task):
    """
    makes employee request and returns json dict response
    """
    url = 'https://jsonplaceholder.typicode.com'
    info = '{}{}{}'.format(url, val, task)
    return requests.get(info).json()


def user_(task):
    """
    makes request for info about employee todo list, then prints
    """
    user = _request('/users/', task)
    todo = _request('/todos/?userId=', task)
    done = [i.get('title') for i in todo if i.get('completed')]
    all = len(todo)
    print('Employee {} is done with tasks({}/{}):'.format(
        user.get('name'), len(done), all))
    for i in done:
        print('\t {}'.format(i))


if __name__ == '__main__':
    """main"""
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        user_(sys.argv[1])
