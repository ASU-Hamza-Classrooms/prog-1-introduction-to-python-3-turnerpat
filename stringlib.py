#!/bin/python3

#reverseStr - takes as input a string and returns the reverse of it
def reverseStr(string):
    return string[::-1]

#containsWord - takes as input two strings, containingStr and containedStr,
#and returns "Yes" if containedStr is anywhere within containingStr 
#and returns "No" otherwise
def containsWord(containingStr, containedStr):
    contains = containingStr.__contains__(containedStr)
    if contains:
        return "Yes"
    else:
        return "No"

#isPalindrome - takes as input a string and returns "Yes" if it is
#palindrome and "No" otherwise  
def isPalindrome(string):
    if string == string[::-1]:
        return "Yes"
    else:
        return "No"

#upperCaseStr - takes as input a string and returns the identical string
#with the characters 'a' ... 'z' changed to uppercase
def upperCaseStr(string):
    return string.upper()

