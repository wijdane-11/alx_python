import csv
import requests
import sys

# Task 0: Gather data from an API and export to CSV
def fetch_employee_data(employee_id):
    try:
        # Fetch employee data
        employee_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
        employee_data = employee_response.json()
        user_id = employee_data['id']

        # Fetch TODO list data
        todos_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos")
        todos_data = todos_response.json()

        # Write data to CSV
        filename = f"{user_id}.csv"
        with open(filename, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE'])
            for task in todos_data:
                csv_writer.writerow([user_id, employee_data['username'], task['completed'], task['title']])

        print(f"Data exported to {filename}")
    except Exception as e:
        print("An error occurred:", e)

# Task 1: Correct number of tasks in CSV
def count_tasks_in_csv(id):
    try:
        with open(f"{id}.csv", 'r') as f:
            csv_reader = csv.reader(f)
            num_tasks = sum(1 for row in csv_reader) - 1  # Subtract 1 for header row
            return num_tasks
    except FileNotFoundError as e:
        return str(e)

# Task 2: Correct user ID and username retrieved
def get_user_info(id):
    try:
        with open(f"{id}.csv", 'r') as f:
            csv_reader = csv.reader(f)
            next(csv_reader)  # Skip header row
            first_row = next(csv_reader)
            user_id = first_row[0]
            username = first_row[1]
            return (user_id, username)
    except FileNotFoundError as e:
        return str(e)

# Task 3: Correct output formatting
def get_tasks_info(id):
    try:
        with open(f"{id}.csv", 'r') as f:
            csv_reader = csv.reader(f)
            next(csv_reader)  # Skip header row
            tasks = [f"{row[2]} - {row[3]}" for row in csv_reader]
            return tasks
    except FileNotFoundError as e:
        return str(e)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    # Task 0
    fetch_employee_data(employee_id)

    # Task 1
    num_tasks = count_tasks_in_csv(employee_id)
    print(f"Number of tasks in CSV: {num_tasks}")

    # Task 2
    user_id, username = get_user_info(employee_id)
    print(f"User ID: {user_id}, Username: {username}")

    # Task 3
    tasks = get_tasks_info(employee_id)
    for task in tasks:
        print(task)
