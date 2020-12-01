def lcp(str):
    length_of_str = len(str[0])
    initial_word = str[0]
    for i in range(len(str)):
        if len(str[i]) < length_of_str:
            length_of_str = len(str[i])
            initial_word = str[i]

    #loop through through words leaving 1st one and check for every letter
    word = 0
    sub_str = ''
    while word < length_of_str:
        char = str[0][word]
        for j in range(1, len(str)):
            if str[j][word] != char:
                return sub_str
        sub_str = sub_str + char
        word = word +1
    return sub_str

str = ["flower","flow","flight"]
print(lcp(str))
