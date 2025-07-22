import json

# Load tasks from file if it exists
try:
    with open("tasks.json", "r") as file:
        tasks = json.load(file)
except FileNotFoundError:
    tasks = []

while True:
    print("Choose an option: ")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark task as completed")
    print("4. Delete Task")
    print("5. Exit")

    user_choice = int(input("Pick an option (1-5): "))

    if user_choice == 5:
        # Save tasks to file before exiting
        with open("tasks.json", "w") as file:
            json.dump(tasks, file)
        print("Tasks saved! Goodbye 👋")
        break

    elif user_choice == 1:
        task = input("What is your task?  ")
        tasks.append({
            "Task": task,
            "Completed": False
        })
        print("Task Added")

    elif user_choice == 2:
        for x in tasks:
            if x["Completed"] == True:
                print(x["Task"], "(✅ Completed)")
            else:
                print(x["Task"])

    elif user_choice == 3:
        print("Pick a task to be marked completed")
        for index, x in enumerate(tasks):
            print(index + 1, ".", x["Task"])
        done = int(input("Enter the number of the task you completed: "))
        count = done - 1
        tasks[count]["Completed"] = True
        print("Marked as completed ✅")

    elif user_choice == 4:
        print("These are all of your tasks to remove")
        for index, x in enumerate(tasks):
            print(index + 1, ".", x["Task"])
        remove_task = int(
            input("Please pick the number of the task you want to remove: "))
        tasks.pop(remove_task - 1)
        print("Updated task list:")
        for x in tasks:
            print(x["Task"])
