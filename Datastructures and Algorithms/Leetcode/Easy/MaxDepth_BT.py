#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 16:06:46 2020
Given the root of a binary tree, return its maximum depth
@author: arpit
"""
from BT import BT,Node

maxd = 0

def maxDepth1(node):
    if node is None:
        return 0
    else:
        return 1+max(maxDepth1(node.left),maxDepth1(node.right))

def maxDepth2(node, d):
    global maxd
    if node is None:
        return 0
    else:
        if d > maxd:
            maxd = d
        d1 = maxDepth2(node.left, d+1)
        d2 = maxDepth2(node.right, d+1)
        return maxd

if __name__ == "__main__":
    
    t = BT()

    nodes = [10,6,12,4,25,11,14,15]

    for i in nodes:
        if i == 10:
            n = Node(i)
            t.insert(n)
        else:
            t.insert(Node(i))
    print(maxDepth2(n, 1))