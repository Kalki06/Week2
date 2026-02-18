def menu():
    print("Enter C for celsius to fahrenheit")
    print("Enter F for fahrenheit to celsius")
    print("Enter E for exit")

def celsius_to_fahrenheit(c):
    F = (c * 9/5) + 32
    return F

def fahrenheit_to_celsius(f):
    C = (f - 32) * 5/9
    return C
while True:
    menu()
    choice = input("Enter your choice : ")

    if(choice == 'C' or choice =='c'):
        temp = int(input("Enter temperature to convert :  "))
        result = celsius_to_fahrenheit(temp)
        print(result)
        break

    elif(choice == 'F' or choice =='f'):
        temp = int(input("Enter temperature to convert :  "))
        result = fahrenheit_to_celsius(temp)
        print(result)
        break

    elif(choice == 'E' or choice =='e'):
        print("Exiting")
        break
    
    else:
        print("Warning ! please enter valid choice only.")
        continue