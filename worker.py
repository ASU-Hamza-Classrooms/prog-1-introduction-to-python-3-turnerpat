#!/bin/python3

from stringlib import *

class Worker:
    def __init__(self, string):
        self.string = string
    
    def reverse(self):
        return reverseStr(self.string)

    def contains(self, contained):
        return containsWord(self.string, contained)

    def palindrome(self):
        return isPalindrome(self.string)

    def upper(self):
        return upperCaseStr(self.string)

