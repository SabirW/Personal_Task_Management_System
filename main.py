from task_manager import TaskManager

def show_menu():
    print("\n=== Personal Task Management System ===")
    print("1. Create a new task")
    print("2. Display all tasks")
    print("3. Mark task as completed")
    print("4. Remove a task")
    print("5. Exit application")

def main():
    manager = TaskManager()

    while True:
        show_menu()
        choice = input("Please select an option (1-5): ")

        if choice == "1":
            description = input("Enter task description: ")
            priority = input("Enter task priority (Low / Medium / High): ")
            manager.add_task(description, priority)

        elif choice == "2":
            manager.list_tasks()

        elif choice == "3":
            try:
                number = int(input("Enter the task number to complete: "))
                manager.complete_task(number)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        elif choice == "4":
            try:
                number = int(input("Enter the task number to remove: "))
                manager.delete_task(number)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        elif choice == "5":
            print("Thank you for using the Task Management System. Goodbye!")
            break

        else:
            print("Unknown option selected. Please try again.")

if __name__ == "__main__":
    main()
