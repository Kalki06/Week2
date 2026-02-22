def has_min_length(password, min_length):
    if(len(password) >= min_length):
        return True
    else:
        return False
    

def has_digit(password):
    for char in password:
        if char.isdigit():
            return True
    return False

def has_uppercase(password):
    for char in password:
        if char.isupper():
            return True
    return False

def check_password_strength(password):

    length = has_min_length(password, 8)
    digit = has_digit(password)
    upper = has_uppercase(password)

    strong = length and digit and upper


    condition = {
        "Length" : length,
        "Digit" : digit,
        "UpperCase" : upper,
        "Strong" : strong
    }
    
    return condition

def main():
    
        while True:
            password = input("Enter your Password : ")

            condition_dict = check_password_strength(password)
            for key, values in condition_dict.items():
                print(f"{key} : {values}\n")

            user_input = input("If you want to exit enter 0 or to continue enter 1: ")
            if(user_input == "0"):
                break
            

if __name__ == "__main__":
    main()

