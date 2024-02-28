import csv
import sys

# Task 0: Correct number of tasks in CSV
def count_tasks_in_csv(id):
    try:
        with open(f"{id}.csv", 'r') as f:
            csv_reader = csv.reader(f)
            num_tasks = sum(1 for row in csv_reader) - 1  # Subtract 1 for header row
            return num_tasks
    except FileNotFoundError as e:
        return str(e)

# Task 1: Correct user ID and username retrieved
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

# Task 2: Correct output formatting
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
    num_tasks = count_tasks_in_csv(employee_id)
    print(f"Number of tasks in CSV: {num_tasks}")

    # Task 1
    user_id, username = get_user_info(employee_id)
    print(f"User ID: {user_id}, Username: {username}")

    # Task 2
    tasks = get_tasks_info(employee_id)
    for task in tasks:
        print(task)
