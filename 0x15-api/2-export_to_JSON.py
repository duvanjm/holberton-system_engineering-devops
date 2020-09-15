#!/usr/bin/python3
"""Write a Python script that, using this
REST API, for a given employee ID"""

import requests
import sys
import json
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
    all_tasks = [
        {'task': i.get('title'),
         'completed': i.get('completed'),
         'username': user_name}
        for i in todo
    ]
    data = {task: all_tasks}
    filename = task + '.json'
    with open(filename, 'w') as f:
        f.write(json.dumps(data))

if __name__ == '__main__':
    """main"""
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        user_(sys.argv[1])
