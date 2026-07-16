def menu():
    print("To do list manager")
    print("1. Add task")
    print("2. View task")
    print("3. Remove task")
    print("4. Quit")
def add_task(tasks):
    task = input("Enter task: ")
    tasks.append(task)
def view_tasks(tasks):
    print("Your Tasks:")
    count = 1
    for task in tasks:
        print(count, ".", task)
        count += 1
    if len(tasks) == 0:
        print("Your task list is empty.")
def remove_task(tasks):
    task = input("Enter task to remove: ")
    if task in tasks:
       tasks.remove(task)
       print("Task removed!")
    else:
        print("Task not found")
tasks = []
choice = " "
while choice != "4":
    menu()
    choice = input("Enter choice: ")
    if choice == "1":
        add_task(tasks)
    elif choice == "2":
        view_tasks(tasks)
    elif choice == "3":
        remove_task(tasks)
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please choose between 1 and 4")
print("Program Ended, Thank you!")