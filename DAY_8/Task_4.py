def taking_input():
    while True:
        try:          
            num1 = int(input("Enter your first number : "))
            num2 = int(input("Enter your second number : "))
            break
        except ValueError:
            print("Enter only integers please !!")
            continue
    return num1, num2

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def multiply(a, b):
    return a*b

def divide(a, b):
    if(b == 0):
        return "None"
    return a / b
    

def menu():
    print("Enter 1 for addition.")
    print("Enter 2 for subtract.")
    print("Enter 3 for multiply.")
    print("Enter 4 for divide.")
    print("Enter 5 for exit.")

def choice():
    choice = int(input("Enter here your choice : "))
    return choice


    
    
while True:
    menu()
    choice1 = choice()
    
    if(choice1 == 1):
        a, b = taking_input()
        result = add(a, b)
        print(result)
    elif(choice1 == 2):
        a, b = taking_input()
        result = sub(a, b)
        print(result)
    elif(choice1 == 3):
        a, b = taking_input()
        result = multiply(a, b)
        print(result)
    elif(choice1 == 4):
        a, b = taking_input()
        result = divide(a, b)
        print(result)
    elif(choice1 == 5):
        print("Exiting !")
        break
    else:
        print("Enter the correct option please !")