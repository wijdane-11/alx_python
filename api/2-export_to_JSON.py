#!/usr/bin/env python3
"""
This script fetches employee data and their TODO list from a REST API and exports it to a JSON file.

The JSON data format:
{
    "USER_ID": [
        {
            "task": "TASK_TITLE",
            "completed": TASK_COMPLETED_STATUS,
            "username": "USERNAME"
        },
        ...
    ]
}

Usage: python3 script.py <employee_id>
"""

import sys
import requests
import json

class EmployeeDataExporter:
    """
    Class responsible for fetching employee data and exporting it to JSON.
    """

    def __init__(self):
        pass

    def fetch_employee_data(self, employee_id):
        """
        Fetches employee data and their TODO list from a REST API and exports it to a JSON file.

        Args:
            employee_id (int): The ID of the employee whose data needs to be fetched.

        Returns:
            None
        """
        try:
            # Fetch employee data
            employee_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
            employee_data = employee_response.json()
            user_id = employee_data['id']
            username = employee_data['username']

            # Fetch TODO list data
            todos_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos")
            todos_data = todos_response.json()

            # Prepare JSON data
            json_data = {str(user_id): [{"task": task['title'], "completed": task['completed'], "username": username} for task in todos_data]}

            # Write data to JSON file
            filename = f"{user_id}.json"
            with open(filename, 'w') as json_file:
                json.dump(json_data, json_file, indent=4)

            print(f"Data exported to {filename}")
        except Exception as e:
            print("An error occurred:", e)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    # Instantiate EmployeeDataExporter class
    data_exporter = EmployeeDataExporter()

    # Fetch and export employee data to JSON
    data_exporter.fetch_employee_data(employee_id)
