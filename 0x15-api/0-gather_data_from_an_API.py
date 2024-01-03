#!/usr/bin/python3
"""A Python script that, for a given employee ID,
returns infomation about his/her TODO list progress.
"""

if __name__ == '__main__':
    import requests
    import sys

    if len(sys.argv) != 2:
        print(f'Usage: {sys.argv[0]} <user_id>', file=sys.stderr)
        exit(1)

    user_id = sys.argv[1]
    url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    name = requests.get(url).json().get('name')

    url = f'https://jsonplaceholder.typicode.com/users/{user_id}/todos'
    tasks = requests.get(url).json()
    done = 0
    tasks_done = []
    for task in tasks:
        if task.get('completed'):
            tasks_done.append(task)
            done += 1

    print(f'Employee {name} is done with tasks({done}/{len(tasks)}):')
    for task in tasks_done:
        print(f'\t {task.get("title")}')
