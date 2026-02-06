class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, priority):
        task = {
            "description": description,
            "priority": priority,
            "completed": False
        }
        self.tasks.append(task)
        print("Task successfully added to your list.")

    def list_tasks(self):
        if not self.tasks:
            print("Your task list is currently empty.")
            return

        for index, task in enumerate(self.tasks, start=1):
            status = "Completed" if task["completed"] else "Pending"
            print(
                f"{index}. {task['description']} "
                f"(Priority: {task['priority']}) [{status}]"
            )

    def complete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]["completed"] = True
            print("Nice work! The task has been marked as completed.")
        else:
            print("The task number you entered does not exist.")

    def delete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f"Task '{removed_task['description']}' was removed.")
        else:
            print("Unable to delete task. Please check the task number.")
