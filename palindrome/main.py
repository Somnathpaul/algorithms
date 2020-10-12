def palindrome(num):
    negative  = num<0
    if negative == True:
        return False
    temp = num
    rev = 0
    while num !=0:
        rev = rev * 10 + num % 10
        num = num // 10
    if rev == temp:
        return True
    else:
        return False
print(palindrome(-121))