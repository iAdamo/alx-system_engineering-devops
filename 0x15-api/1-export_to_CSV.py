#!/usr/bin/python3
"""A Python script that, for a given employee ID,
export infomation about his/her TODO list progress data in the CSV format.
"""
if __name__ == '__main__':
    import csv
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

    with open(f'{user_id}.csv', 'w', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow([user_id, name, task.get('completed'),
                             task.get('title')])
