def is_palindrome(text):
    text = text.lower()
    no_space_string = text.replace(" ", "")
    reverse_string = no_space_string[::-1]
    if(reverse_string == no_space_string):
        return True
    else:
        return False
    

string = input("Enter a string : ")
print(is_palindrome(string))
