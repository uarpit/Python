#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 12:26:10 2022

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

@author: arpit
"""

def duplicate(nums):
    hs = set()
    for i in nums:
        if i in hs:
            return True
        else:
            hs.add(i)
    return False

print(duplicate([1,2,3,1]))