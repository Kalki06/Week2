import math

def is_prime(n):
    if n <= 1:
        return False
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return "False"
        
    return "True"


num = int(input("Enter a number to check if it is prime or not : "))
result = is_prime(num)
print(result)