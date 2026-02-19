def factorial(n):
    if(n == 0):
        return "None"
    
    else:
        fact = 1
        while (n > 1):
            fact *= n
            n-=1
        return fact




num = int(input("Enter a number to calculate the factorial : "))
result = factorial(num)
print(result)