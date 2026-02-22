def reverse_string(text):
    reverse = " "
    for x in text:
        reverse = x + reverse
    
    return reverse

string = input("Enter a string : ")
print(reverse_string(string))