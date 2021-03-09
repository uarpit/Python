#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 14:37:48 2020

@author: arpit
"""

def check_path(input, start=(0,0)):
    ptr = start
    track=set([])
    for i in input:
        if i == 'N':
            ptr = (ptr[0],ptr[1]+1)
        elif i == 'S':
            ptr = (ptr[0],ptr[1]-1)
        elif i == 'W':
            ptr = (ptr[0]-1,ptr[1])
        elif i == 'E':
            ptr = (ptr[0]+1,ptr[1])
        else:
            print("Wrong input.. ignored {}".format(i))

        if ptr in track:
            return True
        else:
            track.add(ptr)
        
    if ptr in track:
            return True
    else:
        return False


start=(0,0)
input = "NES"
print("The path overlaps: {}".format(check_path(input,start)))