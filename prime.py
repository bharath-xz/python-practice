def is_prime(n):
    #Parity
    if n % 2 == 0:
        Parity = "Even"
    else:
        Parity = "Odd"

    #Divisibility
    if n % 3 == 0 and n % 5 == 0:
        Divisibility = "divisble by 3 and 5"
    elif n % 3 == 0:
        Divisibility = "Divisible by 3"
    elif n % 5 == 0:
        Divisibility = "Divisible by 5"
    else:
        Divisibility = ""    
    
    #Prime number
    if n <= 1 :
        return "neither prime nor composite"
        
    for i in range (2, n):
        if n % i == 0:
               return f"{Parity}" +  (f", {Divisibility}" if Divisibility else "")
           
    return f"{Parity}, prime"

print(is_prime(29))
    
      