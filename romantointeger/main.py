def romantointeger(num):
    total = 0
    i=0

    num_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'M':1000, 'D':500, 'CM':900, 'CD':400, 'XC':90, 'XL':40, 'IX':9, 'IV':4, 'II':2}    
    for i in range(0,len(num)):
        #roman = num[i:i+2]
        #total = total + i 
        #print("i:", i)
        roman = num[i]
        if i > 0:
            new_roman = num[i]
            new_roman_val = num_dict.get(new_roman)
            if new_roman_val> prev_val:
                total  = total - 2*(prev_val)
                #print("calculated")
        if i >= 0:
            prev_val = num_dict.get(roman)
            total = total + prev_val
        
        i+=1
    return total
print("total: ",romantointeger('MCMXCIV'))

