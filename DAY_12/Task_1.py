
def count_vowels(text):
    vowels = "aieouAIEOU"
    count = 0
    for x in text:
        if x in vowels:
            count += 1
    
    return count

string = input("Enter a String : ")
print(count_vowels(string))