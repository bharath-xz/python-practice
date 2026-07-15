def remove_task(tasks):
    task = input("Enter task to remove: ")
    tasks.remove(task)
def view_tasks(tasks):
    print(tasks)
tasks = ["study python", "Go gym", "Buy milk"]
remove_task(tasks)
view_tasks(tasks)