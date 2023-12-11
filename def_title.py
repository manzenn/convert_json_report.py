def title(input: str) -> str:
    string = input
    flag = True
    up_word = []
    for i in range (len(string)):
        if string[i] == " ":
            flag = True
            up_word.append(string[i])
        elif flag == True:
            up_word.append(string[i].upper())
            flag = False
        else:
            up_word.append(string[i])
    return ''.join(up_word)

def title1(input: str) -> str: 
    string = input.split()
    title_words = [word[0].upper() + word[1:] for word in string] 
    return ' '.join(title_words)

test = "тесТОвое задание    для pt"

print(title(test))
print(title1(test))
