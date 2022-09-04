#!/bin/python3

#import the code in string1.py

from stringlib import *
from worker import *
import sys

#Function to test the functions in the stringlib module
def testStringLib(inputStr):
    print("Input string is", inputStr)
    
    reverse = reverseStr(inputStr)
    print("Reverse of string is", reverse)
    
    apple = containsWord(inputStr, "apple")
    print("Does string contain apple?", apple)
    
    banana = containsWord(inputStr, "banana")
    print("Does string contain banana?", banana)
    
    palindrome = isPalindrome(inputStr)
    print("Is string a palindrome?", palindrome) 

    upper = upperCaseStr(inputStr)
    print("Uppercase of string is", upper)

    return

#Function to test the methods in the Worker class in the worker module
def testWorkerClass(inputStr):
    worker = Worker(inputStr) 
    
    print("Input string is", worker.string)

    print("Reverse of string is", worker.reverse())

    print("Does string contain apple?", worker.contains("apple"))

    print("Does string contain banana?", worker.contains("banana"))

    print("Is string a palindrome?", worker.palindrome())

    print("Uppercase of string is", worker.upper())

    return

#check to make sure there is a string command line argument
if (len(sys.argv) < 2):
    print("usage: driver1.py <string>")
else:
    #call the functions that test the library and the Worker class
    print("\nTest stringlib:")
    testStringLib(sys.argv[1])
    print("\nTest Worker class:")
    testWorkerClass(sys.argv[1])




