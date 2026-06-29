def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a/b
def show_menu():
    print("Simple Calculator")
    print("1. Add")
    print("2. subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Quit")
show_menu()
choice = ""
while choice != "5":
    choice = input("Choose: ") 
    if choice == "1":
        a = int(input("First number: "))
        b = int(input("Second number: "))
        print("Result = ", add(a, b))
    elif choice == "2":
        a = int(input("First number: "))
        b = int(input("Second number: "))
        print("Result = ",subtract(a, b))
    elif choice == "3":
        a = int(input("First number: "))
        b = int(input("Second number: "))
        print("Result = ",multiply(a, b))
    elif choice == "4":
        a = int(input("First number: "))
        b = int(input("Second number: "))
        print("Result = ",divide(a, b))
    elif choice == "5":
        pass
    else:
        print("Invalid, please choose between 1 and 5")
    if choice != "5":
        show_menu()
print("Goodbye")