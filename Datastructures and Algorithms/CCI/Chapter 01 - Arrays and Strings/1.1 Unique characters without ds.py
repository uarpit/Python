#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 21:59:03 2020
Determine if a string has all unique characters Without using datastructures
@author: arpit
"""

def str_unq_no_ds(ip):
    """
    Python does not have built-in support for Arrays, but Python Lists can be used instead.
    This function uses list with ascii values as index
    ascii 32(space) - 126(~)
    """
    counter = [0]*95
    
    for i in ip:
        try:
            alpha = ord(i)-32
        except:
            print("Please enter charcacters with ascii values ranging from 32 to 126")
        
        if counter[alpha] >= 1:
            return False
        else:
            counter[alpha] +=1
            
    return True

print(str_unq_no_ds("uniqe+* "))