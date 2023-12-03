#Python program to perform a to-do list project

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task_id = len(self.tasks) + 1
        task = {"id": task_id, "description": description, "completed": False}
        self.tasks.append(task)
        print(f"Task {task_id} added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("To-Do List is empty.")
        else:
            print("To-Do List:")
            for task in self.tasks:
                status = "[x]" if task["completed"] else "[ ]"
                print(f"{task['id']}. {status} {task['description']}")

    def mark_completed(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                print(f"Task {task_id} marked as completed!")
                return
        print("Task not found.")

    def update_description(self, task_id, new_description):
        for task in self.tasks:
            if task["id"] == task_id:
                task["description"] = new_description
                print(f"Task {task_id} description updated successfully!")
                return
        print("Task not found.")

    def remove_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                self.tasks.remove(task)
                print(f"Task {task_id} removed successfully!")
                return
        print("Task not found.")


def main():
    todo_list = ToDoList()

    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Mark Task as Completed\n4. Update Task Description\n5. Remove Task\n6. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            description = input("Enter task description: ")
            todo_list.add_task(description)

        elif choice == "2":
            todo_list.view_tasks()

        elif choice == "3":
            task_id = int(input("Enter task ID to mark as completed: "))
            todo_list.mark_completed(task_id)

        elif choice == "4":
            task_id = int(input("Enter task ID to update description: "))
            new_description = input("Enter new description: ")
            todo_list.update_description(task_id, new_description)

        elif choice == "5":
            task_id = int(input("Enter task ID to remove: "))
            todo_list.remove_task(task_id)

        elif choice == "6":
            print("Exiting the application. Goodbye!")
            break

        else:
            print("Invalid choice. Please choose a valid option.")


if __name__ == "__main__":
    main()
