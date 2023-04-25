#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
---Valid Number---
Have the function ValidNumber(s) take a string parameter s, which will only contain a single element,
and return True if it is a valid number that contains only digits with properly placed decimals and
commas, otherwise return False.

For example: if s is '1,093,222.04' then the program should return True, but if the input is '1,093,22.04'
it should return False. The input may contain characters other than digits.
"""

def ValidNumber(s):
    if s.count('.') > 1:
        return False
    elif s.count('.') == 1:
       integer_part, fractional_part = s.split('.')
       
       for char in fractional_part:
           allowed_chars = '0123456789'
           if char not in allowed_chars:
               return False
       return check_integer_part(integer_part)
    else:
        integer_part = s
        return check_integer_part(integer_part)
        
    return True

    
def check_integer_part(integer_part):
    for char in integer_part:
        allowed_chars_int = ',0123456789'
        if char not in allowed_chars_int:
            return False

    if ',' in integer_part:
        for i in range(1, (len(integer_part) // 4)+1):
            if integer_part[len(integer_part) - 4*i] != ',':
                return False
        
    return True 


 
assert ValidNumber('1000,000') == False
assert ValidNumber('1,000,000.56') == True
assert ValidNumber('1,093,222.04') == True
assert ValidNumber('1,093,22.04') == False
assert ValidNumber('0.232567') == True
assert ValidNumber('2,567.00.2') == False


               
