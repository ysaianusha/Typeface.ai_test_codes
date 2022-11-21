"""An LCD (Liquid Crystal Display) can represent multiple digits between 0 to 9 
If you turn the LCD upside-down, some of the numbers still remain valid numbers. For example, 16 becomes 91, 10 becomes 01, which are valid numbers.
If you index all positive numbers (>0) that can produce valid numbers when you upside down the display 
(like 1st one is 1, 2nd one is 2, 3rd one 5... 7th one is 10), 
Write program to print the ’Nth’ number in the series

Input: 8
Output: 11"""


def valid_rev_digit(n):
    # numbers which are valid when even revesed
    v_nums = ['0','1','2','5','6','8','9']
    step = 0
    num = 0
    while step<n:
        num += 1
        if len([i for i in str(num) if i in v_nums]) == len(str(num)):
            step += 1
        
    return num
n = int(input())
print(valid_rev_digit(n))
