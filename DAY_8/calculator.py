def show_menu():
    print("Enter 1 for Add \n" \
    "Enter 2 for Subtract \n"
    "Enter 3 for Multiply \n"
    "Enter 4 for Divide \n"
    "Enter 5 for Exit \n"
    )

def add(a, b):
    return a+b

def sub(a, b):
    return a-b

def divide(a, b):
    return a/b

def multiply(a, b):
    return a*b

while True:
    show_menu()

    opt = int(input())

    if(opt == 1):
        try:
            num1 = int(input("enter your first number : "))
            num2 = int(input("enter your second number : "))
            print(add(num1, num2), "\n")
        except ValueError:
            print("Please enter only integer values, RETRY ! \n")
            continue

    elif(opt == 2):
        try:
            num1 = int(input("enter your first number : "))
            num2 = int(input("enter your second number : "))
            print(sub(num1, num2) ,  "\n")
        except ValueError:
            print("Please enter only integer values, RETRY !\n")
            continue

    elif(opt == 3):
        try:
            num1 = int(input("enter your first number : "))
            num2 = int(input("enter your second number : "))
            print(multiply(num1, num2), "\n")
        except ValueError:
            print("Please enter only integer values, RETRY !\n")
            continue

    elif(opt == 4):
        try:
            num1 = int(input("enter your first number : "))
            num2 = int(input("enter your second number : "))
            if (num2 ==0):
                print("Error ! dividing zero is not possible\n")
            else:
                print(divide(num1, num2),"\n")
        except ValueError:
            print("Please enter only integer values, RETRY !\n")
            continue
    elif(opt == 5):
        print("Exiting")
        break
    else:
        print("Invalid option please select the valid option.\n")