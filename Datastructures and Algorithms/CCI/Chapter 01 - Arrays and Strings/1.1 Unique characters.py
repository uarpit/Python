#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 21:56:23 2020
Determine if a string has all unique characters
This function converts string into set and compares the length.
len function has a timecomplexity of O(1)
converting it to a set is of timecomplexity of O(n)
@author: arpit
"""

def str_unq(ip):
    
    return len(ip) == len(set(ip))

print(str_unq("uniqee "))