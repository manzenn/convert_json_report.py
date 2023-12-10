def title(string):
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

test = "тесТОвое задание    для pt"
print(title(test))