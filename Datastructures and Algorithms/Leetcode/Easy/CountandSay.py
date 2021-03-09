#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 06:48:29 2020
The count-and-say sequence is a sequence of digit strings defined by the 
recursive formula:

    countAndSay(1) = "1"
    countAndSay(n) is the way you would "say" the digit string from 
       countAndSay(n-1), which is then converted into a different digit string.

@author: arpit
"""
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 0:
            pass
        else:
            p='1'
            for i in range(1,n):
                count=0
                prev = ''
                out = ''
                for x in list(p):
                    if x == prev:
                        count +=1
                    else:
                        if prev != '':
                            out = out + str(count)+prev
                        count = 1
                        prev = x
                prev = x
                out = out + str(count) + prev
                p=out
            return p

if __name__ == "__main__":
    s = Solution()
    print(s.countAndSay(4))