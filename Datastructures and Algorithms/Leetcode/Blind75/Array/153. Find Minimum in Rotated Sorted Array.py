#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 13:23:10 2022

Given the sorted rotated array nums of unique elements, return the minimum element of this array.
You must write an algorithm that runs in O(log n) time.

@author: arpit
"""
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]
        l = 0
        r = len(nums) -1
        while(l<=r):
            if nums[l] <= nums[r]:
                return min(res,nums[l])
            else:
                mid = (l + r) // 2
                res = min(res,nums[mid])
                if nums[l] <= nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
        return res