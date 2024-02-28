#!/usr/bin/env python3

"""
This script fetches tasks associated with user IDs from a dummy API
and exports them to a JSON file in a specific format.

The script takes one or more user IDs as command-line arguments and retrieves tasks
belonging to each user from the JSONPlaceholder API. It then constructs a JSON
representation of the tasks for all users and exports them to a file named todo_all_employees.json.

Example usage:
python3 script.py <user_id_1> <user_id_2> ...
"""

import json
import requests
import sys

class TaskExporter:
    """
    TaskExporter class is responsible for fetching tasks from the API and exporting them to JSON.
    """

    def __init__(self):
        pass

    def fetch_tasks(self, user_id):
        """
        Fetches tasks associated with a specific user ID from the JSONPlaceholder API.

        Args:
            user_id (int): The ID of the user whose tasks are to be fetched.

        Returns:
            list: A list of tasks associated with the specified user ID.
        """
        url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
        response = requests.get(url)
        tasks = response.json()
        return tasks

    def export_to_json(self, user_ids):
        """
        Exports tasks to a JSON file in a specific format for multiple users.

        Args:
            user_ids (list): A list of user IDs.

        Returns:
            None
        """
        data = {}
        for user_id in user_ids:
            tasks = self.fetch_tasks(user_id)
            user_tasks = []
            for task in tasks:
                user_tasks.append({
                    "username": task["username"],
                    "task": task["title"],
                    "completed": task["completed"]
                })
            data[str(user_id)] = user_tasks

        with open("todo_all_employees.json", "w") as file:
            json.dump(data, file, indent=4)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 script.py <user_id_1> <user_id_2> ...")
        sys.exit(1)

    user_ids = [int(user_id) for user_id in sys.argv[1:]]
    exporter = TaskExporter()
    exporter.export_to_json(user_ids)
