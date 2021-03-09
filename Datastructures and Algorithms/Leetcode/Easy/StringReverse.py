#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 14:04:43 2020
String reverse
@author: arpit
"""

def str_rev(st):
    s = list(st)
    str_len = len(s) - 1
    
    for i in range(0,int((str_len/2)) + 1):
        s[i],s[str_len-i] = s[str_len-i],s[i]
    print(''.join(s))
    
str_rev("arthya")