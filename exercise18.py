def remove_task(tasks):
    task = input("Enter task to remove: ")
    if task in tasks:
       tasks.remove(task)
       print("Task removed!")
    else:
        print("Task not found")
def view_tasks(tasks):
    print("Your Tasks:")
    count = 1
    for task in tasks:
        print(count, ".", task)
        count += 1
tasks = ["study python", "Go gym", "Buy milk"]
remove_task(tasks)
view_tasks(tasks)