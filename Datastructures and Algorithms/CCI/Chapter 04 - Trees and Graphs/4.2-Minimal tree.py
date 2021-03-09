#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 09:56:44 2020
Given a sorted array with unique integer elements write an algorithm 
to create a binary search tree with minimal height
@author: arpit
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def build_BST(elements,start,end):
    if end < start:
        return None
    else:
        mid = int((start+end)/2)
        node = Node(elements[mid])
        node.left = build_BST(elements,start,mid-1)
        node.right = build_BST(elements,mid+1,end)
        return node
    
elements = [0,2,4,6,8,10]
head = build_BST(elements,0,len(elements)-1)
print(head.val, head.left.val, head.right.val)