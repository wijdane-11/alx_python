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

    # Ensure all user IDs exist in the output
    for user_id in user_ids:
        if str(user_id) not in data:
            data[str(user_id)] = []

    with open("todo_all_employees.json", "w") as file:
        json.dump(data, file, indent=4)
