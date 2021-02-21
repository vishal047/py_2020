#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 15:51:20 2020

@author: vvyas
"""
'''
# Don't forget to import re!
import re
# Define is_valid_time below:
def is_valid_time(input):
    pattern = re.compile(r"\d{1,2}:\d{2}")
    res = pattern.search(input)
    n = res.group()
    print("time in pattern is", n)
    if n == input:
        return True
    return False

print(is_valid_time("it is 11:10"))


import re
 
def parse_date(input):
    pattern = re.compile("^(\d\d)[,/.](\d\d)[,/.](\d{4})$")
    match = pattern.search(input)
    if match:
        return {
            "d": match.group(1),
            "m": match.group(2),
            "y": match.group(3),
        }
    return None

print(parse_date("11.10.2003"))
print(parse_date("12.11,2004"))
print(parse_date("13/12/2005"))
print(parse_date("11.10.2003547"))
'''
for variable in range(20):
    if variable % 4 == 0:
        print(variable)
    if variable % 16 == 0:
        print('Foo!')