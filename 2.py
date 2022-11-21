"""Given two strings as input, find number of occurrences of last character in second string, in the first string. 
Don't use string library functions for this program

Input: “going to go to goa”, “go”
Output: 5 (last char of str2 is o and it appeared 5 times in str1)"""

def find_l(str1, str2):
    l = str2[-1]
    c = len([i for i in str1 if i == l]) 
    return c
str1 = input()
str2 = input()
print(find_l(str1, str2))
