#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 15:06:05 2022

Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.
The test cases are generated so that the answer will fit in a 32-bit integer.
A subarray is a contiguous subsequence of the array.

@author: arpit
"""
def max_product(nums):
    result = nums[0]
    curr_max = 1
    curr_min = 1
    for i in nums:
        temp_curr_max = curr_max 
        curr_max = max(i,temp_curr_max * i, curr_min * i)
        curr_min = min(i,temp_curr_max * i, curr_min * i)
        result = max(result,curr_max)
    return result

print(max_product([-4,-3,-2]))