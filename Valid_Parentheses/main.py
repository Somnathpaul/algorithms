def valid_parenthesis(str):
    if str.startswith(("]", "}",")" )):
        return False

    open_list = ["[","{","("] 
    #close_list = ["]","}",")"] 
    stack1 = [] 
    stack2 = []
    mapping= { "(" : ")", "{": "}", "[": "]"}

    list_of_str = list(str)
    print(list_of_str)
    for i in list_of_str:
        if i in open_list:
            stack1.append(i)
        else:
            stack2.append(i)
        
    stack1.reverse()
    print("stack 1: ",stack1)
    print("stack 2: ",stack2)
    for i in range(0,len(stack1)):
        str = stack1.pop()
        value = mapping.get(str)
        print(str,value)
        if  value == stack2.pop():
            continue
        else:
            return False
    return True



#print(valid_parenthesis("()"))
print(valid_parenthesis("()[]{}"))
#print(valid_parenthesis("(]"))
#print(valid_parenthesis("([)]"))
print("-"*10)
print(valid_parenthesis("{[]}"))


