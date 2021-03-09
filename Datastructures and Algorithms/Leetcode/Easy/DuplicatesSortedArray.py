#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 15:33:09 2020
Given a sorted array nums, remove the duplicates in-place 
such that each element appears only once and returns the new length.
Do not allocate extra space for another array, you must do this 
by modifying the input array in-place with O(1) extra memory.
@author: arpit
"""
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        for j in range(1,len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i+1
        
        
if __name__ == "__main__":
    s = Solution()
    nums = [0,0,1,1,1,2,2,3,3,4]
    
    for i in range(0,s.removeDuplicates(nums)):
        print(nums[i],end=" ")