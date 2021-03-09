#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 14:28:38 2020
Climbing stairs: It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. 
In how many distinct ways can you climb to the top?
@author: arpit
"""
class Solution:
    def __init__(self):
        self.arr = [-1]
    
    def climbStairs(self,n):
        if n <= 0:
            return 0
        self.arr = self.arr*(n+1)
        return self.climb_iter(n)
    
    # uses recursion
    def climb(self,n):
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            if self.arr[n-1] == -1:
                self.arr[n-1] = self.climb(n-1)
            if self.arr[n-2] == -1:
                self.arr[n-2] = self.climb(n-2)
            return self.arr[n-1] + self.arr[n-2]
    
    #uses iteration - It is like solving fibonacci series
    def climb_iter(self,n):
        if n == 1:
            self.arr[n] = 1
        elif n == 2:
            self.arr[n] = 2
        else:
            self.arr[1] = 1
            self.arr[2] = 2
            for i in range(3,n+1):
                self.arr[i] = self.arr[i-1] + self.arr[i-2]
                                
        return self.arr[n]
                
if __name__ == "__main__":
    s = Solution()
    print(s.climbStairs(5))
        
