#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 17:00:16 2020
Given an integer n, return true if it is a power of three. Otherwise, 
return false.
An integer n is a power of three, if there exists an integer x such that n == 3x.
@author: arpit
"""
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        count = 0
        while n > 1:
            if n%3 == 0:
                n /= 3
                count +=1
            else:
                return False
        return n==1 
    
if __name__ == "__main__":
    s = Solution()
    print(s.isPowerOfThree(29))