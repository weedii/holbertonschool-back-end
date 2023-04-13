#!/usr/bin/python3

"""Gather data from an API"""

import csv
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

    filename = f"{id}.csv"
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        for i in todos:
            f.write(
                f"\"{i['userId']}\",\"{employee_name}\","
                f"\"{i['completed']}\",\"{i['title']}\"\n")
