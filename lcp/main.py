def lcp(str):
    length_of_str = len(str[0])
    initial_word = str[0]
    for i in range(len(str)):
        #print(len(str[i]))
        if len(str[i]) < length_of_str:
            length_of_str = len(str[i])
            initial_word = str[i]

    #return length_of_str
    word = 0
    sub_str = ''
    while word < len(str):
        for i in str[word]:
            for j in range(len(initial_word)):
                if i == initial_word[j]:
                    sub_str = sub_str + i
                    print(sub_str)
        word = word+1
        print(word)
    print("-")

str = ["flower","flow","flight"]
print(lcp(str))
