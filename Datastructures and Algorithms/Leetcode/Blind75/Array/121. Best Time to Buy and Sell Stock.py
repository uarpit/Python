#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 12:12:02 2022

You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

@author: arpit
"""
def BuySell(price):
    m = 0
    curr = 0
    for i in range(1,len(price)):
        curr += price[i] - price[i-1]
        #print(curr)
        if curr < 0:
            curr = 0
        m = max(m,curr)
    return m

print(BuySell([7,1,5,3,6,4]))
        