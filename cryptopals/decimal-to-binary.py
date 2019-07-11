def decimal_to_binary(n):  
    if(n > 1):  
        decimal_to_binary(n//2)     
    print(n%2, end='')

print("69 in binary is: ")
decimal_to_binary(69)
