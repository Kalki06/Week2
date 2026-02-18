def calculate_simple_interest(p, r, t):
    SI = (p*r*t)/100
    return SI

principal = int(input("Enter the principle amount : "))
rate  = int(input("Enter the interest rate : "))
time  = int(input("Enter investing time in years : "))

Interest_Amount = calculate_simple_interest(principal, rate, time)
print(Interest_Amount)