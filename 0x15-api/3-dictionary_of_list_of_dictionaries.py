#!/usr/bin/python3
"""Write a Python script that, using this
REST API, for a given employee ID"""

import requests
import json


def _request(val, task):
    """reques for user"""
    url = 'https://jsonplaceholder.typicode.com'
    info = '{}{}{}'.format(url, val, task)
    return requests.get(info).json()


def user_():
    """reques for user"""
    employee = {}
    _url = 'https://jsonplaceholder.typicode.com/users/'
    user = requests.get(_url).json()
    for u in user:
        task = str(u.get('id'))
        user_name = u.get('username')
        todo = _request('/todos/?userId=', task)
        all_tasks = [
            {'username': user_name,
             'task': i.get('title'),
             'completed': i.get('completed')}
            for i in todo
        ]
        employee[task] = all_tasks
    filename = 'todo_all_employees.json'
    with open(filename, 'w') as f:
        f.write(json.dumps(employee, sort_keys=True))


if __name__ == '__main__':
    """main"""
    user_()
