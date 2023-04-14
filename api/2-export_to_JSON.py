#!/usr/bin/python3

"""Gather data from an API"""

import json
import requests
import sys

if __name__ == "__main__":

    id = sys.argv[1]
    response = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{id}/todos")
    todos = response.json()

    completed_tasks = [todo for todo in todos if todo["completed"]]

    response = requests.get(f"https://jsonplaceholder.typicode.com/users/{id}")
    employee_name = response.json()["username"]

    lis_of_dic = []
    for i in todos:
        dic = {"task": i['title'], "completed": i['completed'],
               "username": employee_name}
        lis_of_dic.append(dic)

    final_dc = {id: lis_of_dic}

    filename = f"{id}.json"
    with open(filename, 'w', newline='') as f:
        json.dump(final_dc, f)
