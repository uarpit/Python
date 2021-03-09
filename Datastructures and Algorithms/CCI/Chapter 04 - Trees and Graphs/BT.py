#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 16:22:29 2020
Program to make build a Binary Tree - Not Binary search tree

@author: arpit
"""
from collections import defaultdict,deque

class Node:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

class BT:
    def __init__(self):
        self.root = None
        self.q = deque()
        
    def insert(self,nd):
        if self.root == None:
            self.root = nd
            self.q.append(nd)
        else:
            #print(self.q[0].val)
            if self.q[0].left is None:
                self.q[0].left = nd
                self.q.append(nd)
            elif self.q[0].right is None:
                self.q[0].right = nd
                self.q.append(nd)
            else:
                self.q.popleft()
                #print(t.val)
                self.q[0].left = nd
                self.q.append(nd)
                
if __name__ == "__main__":
    
    t = BT()

    nodes = [10,6,12,4,25,11,14]

    for i in nodes:
        t.insert(Node(i))
    print(t.root.left.right.val)
                
        
