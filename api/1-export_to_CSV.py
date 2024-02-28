import sys
import requests
import csv

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

        # Write data to CSV
        filename = f"{user_id}.csv"
        with open(filename, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE'])
            for task in todos_data:
                csv_writer.writerow([user_id, username, task['completed'], task['title']])

        print(f"Data exported to {filename}")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    fetch_employee_data(employee_id)
