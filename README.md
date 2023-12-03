# motion-cut-python-programming-intern

"ToDoList" Class:

Constructor ('__init__' method):
   > Initializes an instance of the 'ToDoList' class.
   > Creates an empty list ('self.tasks') to store tasks.

'add_task' method:
   > Takes a description as input.
   > Generates a unique 'task_id' based on the current number of tasks.
   > Creates a dictionary representing a task with keys "id," "description," and "completed."
   > Appends the task to the tasks list.
   > Prints a success message indicating the task addition.

'view_tasks' method:
   > Checks if the tasks list is empty.
   > If empty, prints a message indicating an empty to-do list.
   > If not empty, prints each task's ID, completion status, and description.

'mark_completed' method:

   > Takes a task_id as input.
   > Iterates through the tasks and marks the task with the specified ID as completed.
   > Prints a success message if the task is found and marked completed, otherwise prints an error message.

'update_description' method:
> Takes a 'task_id' and a 'new_description' as input.
    Iterates through the tasks and updates the description of the task with the specified ID.
      Prints a success message if the task is found and the description is updated, otherwise prints an error message.

'remove_task' method:
> Takes a task_id as input.
    Iterates through the tasks and removes the task with the specified ID.
    Prints a success message if the task is found and removed, otherwise prints an error message.


'main' Function:

Instantiates 'ToDoList' object:
 > Creates an instance of the ToDoList class named todo_list.

Main Execution Loop:
 > Runs an infinite loop that presents a menu to the user until they choose to exit.

Menu Options:
  > Option 1 ("Add Task"): Takes a task description from the user and adds it to the to-do list.
   Option 2 ("View Tasks"): Displays the current tasks in the to-do list.
   Option 3 ("Mark Task as Completed"): Takes a task ID and marks the corresponding task as completed.
    Option 4 ("Update Task Description"): Takes a task ID and a new description, updating the task's description.
    Option 5 ("Remove Task"): Takes a task ID and removes the corresponding task from the to-do list.
    Option 6 ("Exit"): Exits the application.

Error Handling:
> Prints an error message for invalid menu choices.

'__name__ == "__main__"' Block:
   > Checks if the script is being run as the main program.
   > If true, calls the 'main' function, initiating the execution of the to-do list application.
