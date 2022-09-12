#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 13:18:59 2022

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
A subarray is a contiguous part of an array.

@author: arpit
"""

def maxSubarray(nums):
    max_all = nums[0]
    curr = nums[0]
    for i in range(1,len(nums)):
        curr = max(curr+nums[i],nums[i])
        max_all = max(curr,max_all)
    return max_all

print(maxSubarray([-2,1,-3,4,-1,2,1,-5,4]))