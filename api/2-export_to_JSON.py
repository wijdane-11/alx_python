import sys
import requests
import json

def fetch_employee_data(employee_id):
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
    fetch_employee_data(employee_id)