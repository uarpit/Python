#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 16:02:39 2020
Given a non-empty array of integers nums, 
every element appears twice except for one. Find that single one.
@author: arpit
"""

def single_num(nums):
    
    out = 0
    for i in nums:
        out ^= i
    return out

nums = [4,1,2,1,2,5,4]
print(single_num(nums))