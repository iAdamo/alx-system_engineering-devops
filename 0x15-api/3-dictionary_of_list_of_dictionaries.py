#!/usr/bin/python3
"""A Python script that, for a given employee ID,
export infomation about his/her TODO list progress data in the JSON format.
"""
from urllib import response


if __name__ == '__main__':
    import json
    import requests

    with open(f'todo_all_employees.json', 'w', encoding='utf-8') as jsonfile:
        url = f'https://jsonplaceholder.typicode.com/users'
        users = requests.get(url).json()
        dicts = {}
        for user in users:
            base_url = 'https://jsonplaceholder.typicode.com/users/{}'
            url = '{}/todos'.format(base_url.format(user.get("id")))
            tasks = requests.get(url).json()
            dicts.update({user.get('id'): [{
                'username': user.get('username'),
                'task': task.get('title'),
                'completed': task.get('completed'),
                } for task in tasks]})
        json.dump(dicts, jsonfile, indent=2)
