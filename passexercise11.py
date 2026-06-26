def count_uppercase(password):
    count = 0
    for char in password:
        if char.isupper():
            count +=1
    return count 
password = "CyberSEC123"
print(count_uppercase(password))