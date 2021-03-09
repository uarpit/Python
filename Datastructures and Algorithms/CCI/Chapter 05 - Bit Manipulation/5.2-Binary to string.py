#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given a real number between 0 and 1. print binary replresentation 
if it fits in 32 bit else print ERROR
"""

def convert(i):
    output=""
    while(len(output)<31):
        i *=2
        if i >= 1:
            output = output + "1"
            i -= 1
        elif i>0 and i<1:
            output = output + "0"
        if i==0:
            return output
    return "Error"
            

x=0.625
print(convert(x))

