#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 13:13:19 2020
Given an integer array nums, find the contiguous subarray 
(containing at least one number) which has the largest sum and return its sum.
@author: arpit
"""
import math
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_all = float('-inf')
        max_sofar = float('-inf')
        for i in nums:
            max_sofar = max(max_sofar+i,i)
            max_all = max(max_sofar,max_all)
        return max_all
    
if __name__ == "__main__":
    s = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(s.maxSubArray(nums))