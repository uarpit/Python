#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 13:10:23 2020
Implement a functionto check if a binary tree is balanced. 
Heights of two subtree should not differ by more than 1
@author: arpit
"""
from BST import BST, Node

class checkBalanced:
    def __init__(self):
        self.min = float('inf')
        self.max = 0
        
    def traverse(self,nd, d=0): #d for depth
        if nd is None:
            if d < self.min:
                self.min = d
            if d > self.max:
                self.max = d
        else:
            self.traverse(nd.left,d+1)
            self.traverse(nd.right,d+1)
    
    def check(self):
        return self.max - self.min <= 1
    

if __name__ == "__main__":
    t = BST()

    nodes = [1,4,6]

    for i in nodes:
        t.insert(Node(i))
    t.delete(4)
    
    cb = checkBalanced()
    cb.traverse(t.root)
    print("The tree is balanced - {}".format(cb.check()))
