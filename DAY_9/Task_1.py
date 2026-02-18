def calculate_area(a, b):
    return a * b

length = int(input("Enter the length of rectangle : "))
width = int(input("Enter the width of rectangle : "))

area = calculate_area(length, width)
print(area)