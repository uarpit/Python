#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 18:45:47 2020
Implementing Binary search tree
@author: arpit
"""

class Node:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None
    
class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, nd):
        tmp = self.root
        prev = None
        while(tmp is not None):
            prev = tmp
            if nd.val < tmp.val:
                tmp = tmp.left
            else:
                tmp = tmp.right
    
        if prev is None:
            self.root = nd
            return
        if nd.val < prev.val:
            prev.left = nd
        else:
            prev.right = nd
    
    def mintree(self,prev,start):
        p=prev
        ptr=start
        while(ptr.left is not None):
            p=ptr
            ptr=ptr.left
        return (p,ptr)
    
    def transplant(self,prev,u,v):
        if prev is None:
            self.root = v
        else:
            if prev.left == u:
                prev.left = v
            else:
                prev.right = v
    
    
    def delete(self, val):
        tmp = self.root
        prev = None
        while(tmp is None or tmp.val != val):
            prev = tmp
            if val < tmp.val:
                tmp = tmp.left
            else:
                tmp = tmp.right
            
        if tmp.left is None:
            self.transplant(prev,tmp,tmp.right)
        elif tmp.right is None:
            self.transplant(prev,tmp,tmp.left)
        else:
            pmin,nextmin=self.mintree(tmp,tmp.right)
            if tmp.right.val != nextmin.val:
                self.transplant(pmin,nextmin,nextmin.right)
                nextmin.right = tmp.right
            
            nextmin.left = tmp.left
            self.transplant(prev,tmp,nextmin)
                
        
            
            

if __name__ == "__main__":
    t = BST()

    nodes = [5,2,8,1,4,6,9,7]

    for i in nodes:
        t.insert(Node(i))
    t.delete(2)

