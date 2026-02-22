def count_words(sentence):
    count = 0
    inside_word = False 

    for x in sentence:
        if(x != " "):
            if not inside_word:
                count += 1
                inside_word  = True
        else:
            inside_word = False
    return count

string = input("Enter a sentence : ")
print(count_words(string))