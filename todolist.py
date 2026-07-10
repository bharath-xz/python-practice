def menu():
    print("To do list manager")
    print("1. Add task")
    print("2. View task")
    print("4. Quit")
def add_task(tasks):
    task = input("Enter task: ")
    tasks.append(task)
def view_tasks(tasks):
    print(tasks)
tasks = []
choice = " "
while choice != "4":
    menu()
    choice = input("Enter choice: ")
    if choice == "1":
        add_task(tasks)
    elif choice == "2":
        view_tasks(tasks)
    if choice == "4":
        break
print("Program Ended, Thank you!")