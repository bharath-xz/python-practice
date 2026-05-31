for i in range(1, 31):
    if i % 5 == 0 and i % 3 == 0:
        print(f"{i} is divisible by 3 and 5", end="")   
    elif i % 3 == 0:
        print(f"{i} is divisible by 3", end="")   
    elif i % 5 == 0:
        print(f"{i} is divisible by 5", end="")               
    else:
        print(f"{i} is not special", end="")

    if i % 2 == 0:
        print(" and even")     
    else:
        print(" and odd")    
