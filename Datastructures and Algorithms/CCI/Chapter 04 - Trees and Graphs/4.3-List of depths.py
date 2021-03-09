#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 11:54:17 2020
Given a binary tree, design an algorithm which creates linkedlist of all the nodes
at each depth
@author: arpit
"""
#from BST import BST
from BST_P import BST_P

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
        self.next = None
        
class LinkTree:
    def __init__(self):
        self.depthlist = []
        
    def traverse(self,node,d=0):
        if node is None:
            return None
        else:
            #print(node.val, "Traverse")
            try:
                ptr = self.depthlist[d]
                self.addlink(ptr,node)
            except:
                self.depthlist.append(node)
            
            #print(node.val)
            self.traverse(node.left,d+1)
            self.traverse(node.right,d+1)
    
    def addlink(self,ptr,nd):
        while ptr.next is not None:
            ptr = ptr.next
        ptr.next = nd
    

if __name__ == "__main__":
    t = BST_P()

    nodes = [5,2,8,1,4,6,9,7]

    for i in nodes:
        t.insert(Node(i))
    t.delete(2)
    lt = LinkTree()
    lt.traverse(t.root)
    for i in lt.depthlist:
        tmp = i
        while tmp.next is not None:
            print(tmp.val,end="->")
            tmp = tmp.next
        print(tmp.val)
