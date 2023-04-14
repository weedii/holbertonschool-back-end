#!/usr/bin/python3

"""Dictionary of list of dictionaries"""

import json
import requests
import sys

if __name__ == "__main__":

    user_data = requests.get(
        "https://jsonplaceholder.typicode.com/users/").json()
    todos_data = requests.get(
        "https://jsonplaceholder.typicode.com/todos/").json()

    final_of_final = {}
    for u in user_data:
        user_id = u['id']
        if user_id not in final_of_final:
            final_of_final[user_id] = []

        for t in todos_data:
            if user_id == t['userId']:
                dc = {"username": u['username'],
                      "task": t['title'], "completed": t['completed']}
                final_of_final[user_id].append(dc)

    with open("todo_all_employees.json", 'w') as f:
        json.dump(final_of_final, f)
