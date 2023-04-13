#!/usr/bin/python3

"""Gather data from an API"""


import requests
import json
import sys


id = sys.argv[1]
user_response = requests.get("https://jsonplaceholder.typicode.com/users/"+id)
todos_response = requests.get("https://jsonplaceholder.typicode.com/todos")


user_data = user_response.json()
todos_data = todos_response.json()

nbr_task = 0
nbr_cpt_task = 0
title_task = []

for i in todos_data:
    if i["userId"] == int(id):
        nbr_task += 1
        if i["completed"] == 1:
            title_task.append(i["title"])


print(
    f"Employee {user_response.json().get('name')} is done with tasks ({len(title_task)}/{nbr_task}):")

for i in title_task:
    print(f"\t{i}")
