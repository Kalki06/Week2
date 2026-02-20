import math

def is_prime(n):
    if(n <= 1):
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if(n%i == 0):
            return False
    return True

def is_even(n):
    if(n%2 == 0):
        return True
    return False

def factorial(n):
    if (n <= 0):
        return None
    else:
        fact = 1
        for i in range(1, n+1):
            fact *= i
        return fact


def menu():
    while True:
        print("Enter 1 for checking if a number is prime or not : \n")
        print("Enter 2 for checking if a number is even or not : \n")
        print("Enter 3 for calculating the factorial : \n")
        print("Enter 4 for exiting : \n")
        try:
            choice = int(input())
        except ValueError:
            print("Please enter valid option from the menu only: \n")
            continue
        
        if(choice >=1 and choice <= 4):
            return choice
        else:
            print("Please enter valid option from the menu only: \n")

def user_input():
    while True:
        try:
            num = int(input("Enter a number : "))
            return num
        except ValueError:
            print("Enter only integer please")
            continue


def main():

    while True:
        user_choice = menu()

        if(user_choice == 1):
            num = user_input()
            prime = is_prime(num)
            print(prime)
            continue

        elif(user_choice == 2):
            num = user_input()
            even = is_even(num)
            print(even)
            continue

        elif(user_choice == 3):
            num = user_input()
            fact = factorial(num)
            print(fact)
            continue

        else:
            print("Exiting")
            break
    
if __name__ == "__main__":
    main()