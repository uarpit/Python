#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 14:52:16 2020
Implement a function to check if a binary tree is binary search tree
@author: arpit
"""

from BT import BT, Node

prev = None

def checkBST(node):
    global prev
    if node is None:
        return True
    else:
        if prev is not None:
            if prev.val > node.val:
                return False
        l = checkBST(node.left)
        #print(node.val)
        r = checkBST(node.right)
        try:
            print(prev.val, node.val)
        except:
            pass
        prev = node
        return (l and r)
    
if __name__ == "__main__":
    
    t = BT()

    nodes = [10,6,12,4,25,11,14]

    for i in nodes:
        t.insert(Node(i))
    #t.delete(4)
    """
    a = Node(5)
    a.left = Node(6)
    a.right = Node(8)
    """
    
    print(checkBST(t.root))

