import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)-25s %(levelname)-7s %(lineno)-4s %(message)-8s')  
# comment below section to start debuging 
logger = logging.getLogger()
logger.disabled = True


def valid_parenthesis(str):
    logging.debug("check for closing bracket")
    if str.startswith(("]", "}",")" )):
        return False

    open_list = ["[","{","("] 
    stack1 = [] 
    mapping= { "(" : ")", "{": "}", "[": "]"}
    check1 = 0
    check2 = 0

    for i in str:
        if i in open_list:
            stack1.append(i)
            check1 = check1+1
            print("stack1: ", stack1)
        else:
            if len(stack1) != 0:
                check2 = check2 + 1
                st = stack1.pop()
                value = mapping.get(st)
                print("i: ", i)
                print("st: ", st)
                print("value: ", value)
                if i == value:
                    continue
                else:
                    return False
            else:
                return False

    if check1 == check2:
        return True
    else:
        return False
   


'''
print(valid_parenthesis("()"))
print("-"*10)

print(valid_parenthesis("()[]{}"))
print("-"*10)

print(valid_parenthesis("(]"))
print("-"*10)

print(valid_parenthesis("([)]"))
print("-"*10)

print(valid_parenthesis("{[]}"))


print("------ test case ---------")

print(valid_parenthesis( '(('  ))
'''
print("------ test case ---------")
print(valid_parenthesis( '(){}}{'  ))