def calculate_area(a, b):
    return a * b

def calculate_simple_interest(p, r, t):
    SI = (p*r*t)/100
    return SI

def print_table(num):
    for i in range(1, 11):
        print(f"{num} x {i} = {num*i}")

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

def main():
    length = int(input("Enter the length of rectangle : "))
    width = int(input("Enter the width of rectangle : "))
    area = calculate_area(length, width)
    print(area)

    principal = int(input("Enter the principle amount : "))
    rate  = int(input("Enter the interest rate : "))
    time  = int(input("Enter investing time in years : "))
    Interest_Amount = calculate_simple_interest(principal, rate, time)
    print(Interest_Amount)

    number  = int(input("Enter a number to write the table : "))
    print_table(number)

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

if __name__ == "__main__":
    main()