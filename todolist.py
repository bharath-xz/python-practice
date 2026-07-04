def menu():
    print("To-Do List Manager")
    print("1. Add task")
    print("2. View Task")
    print("4. Quit")
def add_task(tasks):
   result = []
   result.append(tasks)
   return result
def view_task(tasks):
    tasks = []
    print(view_task(tasks))
choice = ""
while choice != "4":
    menu()
    choice = input("Enter choice: ")
    if choice == "1":
        tasks = input("Enter task: ")
        print(add_task(tasks))
    elif choice == "2":
        add_task(tasks)
    elif choice == "4":
        break
    if choice > "4":
        print("Invalid option, choose between 1 and 4")
print("Goodbye")
        
        
   