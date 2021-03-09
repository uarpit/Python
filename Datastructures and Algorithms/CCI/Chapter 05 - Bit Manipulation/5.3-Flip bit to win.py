#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Input: Integer. You can flip exactly one bit from 0 to 1
Find the length of longest sequesce of 1s
Note: Not complete yet
"""
def flip_bit(x):
    accept=True
    size=0
    output=[]
    final=[]
    seq=list(bin(x))[2:]
    for i in seq:
        if int(i):
            size +=1
        else:
            if len(output) > 0:
                output.append(size)
                if accept:
                    accept=False
                else:
                    final.append(output)
                    accept = True
                size=0
    final.append(output)
    print(final)

x = 104
print(bin(x))
flip_bit(x)
