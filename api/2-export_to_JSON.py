#!/usr/bin/env python3

"""
This script fetches tasks associated with a specific user ID from a dummy API
and exports them to a JSON file in a specific format.

The script takes a user ID as a command-line argument and retrieves tasks
belonging to that user from the JSONPlaceholder API. It then constructs a JSON
representation of the tasks and exports them to a file named <user_id>.json.

Example usage:
python3 script.py <user_id>
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

    def export_to_json(self, user_id, tasks):
        """
        Exports tasks to a JSON file in a specific format.

        Args:
            user_id (int): The ID of the user.
            tasks (list): A list of tasks associated with the user.

        Returns:
            None
        """
        data = {str(user_id): []}
        for task in tasks:
            data[str(user_id)].append({
                "task": task["title"],
                "completed": task["completed"],
                "username": task["username"]
            })
        with open(f"{user_id}.json", "w") as file:
            json.dump(data, file, indent=4)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <user_id>")
        sys.exit(1)

    user_id = int(sys.argv[1])
    exporter = TaskExporter()
    tasks = exporter.fetch_tasks(user_id)
    exporter.export_to_json(user_id, tasks)
