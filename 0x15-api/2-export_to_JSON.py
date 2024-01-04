#!/usr/bin/python3
"""A Python script that, for a given employee ID,
export infomation about his/her TODO list progress data in the JSON format.
"""
if __name__ == '__main__':
    import json
    import requests
    import sys

    if len(sys.argv) != 2:
        print(f'Usage: {sys.argv[0]} <user_id>', file=sys.stderr)
        exit(1)

    user_id = sys.argv[1]
    url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    name = requests.get(url).json().get('username')

    url = f'https://jsonplaceholder.typicode.com/users/{user_id}/todos'
    tasks = requests.get(url).json()

    with open(f'{user_id}.json', 'w', encoding='utf-8') as jsonfile:
        json.dump({user_id: [{
            'task': task.get('title'),
            'completed': task.get('completed'),
            'username': name
        } for task in tasks]}, jsonfile, indent=2)
