password = input("Enter your password").strip()
errors = []
if len(password) < 8:
    errors.append("must be atleast 8 charactes")

if not any(char.isdigit() for char in password) :
    errors.append("must containat least one number")

if not any(char.isupper() for char in password) :
    errors.append("must contain at least one uppercase letter")

if errors:
    print("Weak password")
    print("isuues:")
    for err in errors:
        print(err)

else:
    print("Strong password ")    