#!/usr/bin/python3

"""Write a Python script that, using this
REST API, for a given employee ID"""

import requests
import json


if __name__ == "__main__":
    req = requests.get('https://jsonplaceholder.typicode.com/users')
    users = req.json()
    req = requests.get('https://jsonplaceholder.typicode.com/todos')
    tasks = req.json()
    dic = {str(d.get('id')): [{'username': d.get('username'),
                               'task': i.get('title'), 'completed':
                               i.get('completed')}
                              for i in tasks
                              if i.get('userId') == d.get('id')]
           for d in users}
    with open('todo_all_employees.json', 'w') as f:
        json.dump(dic, f)
