"""
Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−2^31,  2^31 − 1]. 
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

Input: x = 123
Output: 321

Input: x = -123
Output: -321

Input: x = 120
Output: 21

"""

def reverse(x):
    negative = x <0 # returns true / false if the input number is negative 
    x = abs(x) # removes everything except numbers
    rev  = 0
    #print(x)
    while x != 0:
        rev = rev * 10 + x % 10 
        x = x // 10
        #print(rev, x )
        #print("__"* 5)

    if rev > pow(2, 31)-1:
        return 0 
    
    if negative == True :
        return -(rev)
    else:
        return rev 


X = 120

print(reverse(X))
    

