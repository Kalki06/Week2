def fibonacci(n):
    if(n <= 0 ):
        return 0
    else:
        a = 0
        b = 1
        series = [a,b]
        while(len(series) < n): 
            c= a+b
            series.append(c)
            a = b
            b = c
        return series

num = int(input("Enter a number to calculate the factorial : "))
result = fibonacci(num)
print(result)
