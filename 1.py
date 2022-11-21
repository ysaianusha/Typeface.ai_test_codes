# Given an integer as input. Write a function to convert that to base 3 number
def base_3(num):
    if num<0:
        sign = '-'
    else:
        sign = ''
    num = abs(num)
    if num<3:
        return str(num)
    else:
        s = ''
        while num>0:
            s = str(num%3) + s
            num //= 3
    return 0-int(s) if sign=='-' else int(s)
    
# main function
n = int(input())
print( base_3(n))
