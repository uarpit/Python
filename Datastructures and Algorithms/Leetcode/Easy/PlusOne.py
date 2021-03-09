#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 13:53:31 2020
Given a non-empty array of decimal digits representing a non-negative 
integer, increment one to the integer.
The digits are stored such that the most significant digit is at the head 
of the list, and each element in the array contains a single digit.
You may assume the integer does not contain any leading zero, except the number 0 itself.
@author: arpit
"""
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range(len(digits)-1,-1,-1):
            if digits[i] < 9:
                digits[i] +=1
                return digits
            digits[i] = 0
        
        if digits[0]==0:
            digits = [1] + digits
        
        return digits