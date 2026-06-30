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
def get_numbers():
   a = float(input("First number: "))
   b = float(input("Second number: "))
   return a, b
show_menu()
choice = ""
while choice != "5":
    choice = input("Choose: ")
    a, b = get_numbers() 
    if choice == "1":
        print("Result = ", add(a, b))
    elif choice == "2":
        print("Result = ",subtract(a, b))
    elif choice == "3":
        print("Result = ",multiply(a, b))
    elif choice == "4":
        if b == 0:
            print("Cannot divide by zero")
        else:
            print("Result = ",divide(a, b))
    elif choice == "5":
        pass
    else:
        print("Invalid, please choose between 1 and 5")
    if choice != "5":
        show_menu()
print("Goodbye")