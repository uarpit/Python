#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 12:56:17 2022

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

@author: arpit
"""

def productExcept(nums):
    left = nums[:]
    right = nums[:]
    left[0] = 1
    right[len(nums)-1] = 1
    
    for i in range(1,len(nums)):
        left[i] = nums[i-1] * left[i-1]
        
    for i in range(len(nums)-2,-1,-1):
        right[i] = nums[i+1] * right[i+1]
        
    for i in range(len(nums)):
        right[i] *= left[i]
    
    return right

print(productExcept([1,2,3,4]))