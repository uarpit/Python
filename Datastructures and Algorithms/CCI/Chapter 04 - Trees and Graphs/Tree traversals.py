#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tree traversal: This program gives preorder, inorder and postorder traversals
@author: arpit
"""
from BST import BST

class Node:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None
 
def visit(nd):
    if nd is None:
        return
    else:
        print(nd.val,end=" ")
 
def in_order(root):
    if root is not None:
        in_order(root.left)
        visit(root)
        in_order(root.right)
    
def pre_order(root):
    if root is not None:
        visit(root)
        pre_order(root.left)
        pre_order(root.right)
        
def post_order(root):
    if root is not None:
        pre_order(root.left)
        pre_order(root.right)
        visit(root)
        
if __name__ == "__main__":
    t = BST()
 
    nodes = [5,2,7,1,4,6,8]
    for i in nodes:
        t.insert(Node(i))
    
    pre_order(t.root)
    t.delete(2)
    print()
    pre_order(t.root)
    print()
    t.delete(8)
    in_order(t.root)
    print()
    t.delete(5)
    in_order(t.root)
