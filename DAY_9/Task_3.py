def print_table(num):
    for i in range(1, 11):
        print(f"{num} x {i} = {num*i}")

number  = int(input("Enter a number to write the table : "))

print_table(number)