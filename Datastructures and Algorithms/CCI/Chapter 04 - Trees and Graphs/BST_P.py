#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 15:30:12 2020
Write an algorithm to find the next node (in-order successor)
The node has a parent link
@author: arpit
"""
class NodeP:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
        
class BST_P:
    def __init__(self):
        self.root = None
        
    def insert(self,nd):
        if self.root is None:
            self.root = nd
        else:
            ptr = self.root
            prev = None
            while(ptr is not None):
                prev = ptr
                if nd.val < ptr.val:
                    ptr = ptr.left
                else:
                    ptr = ptr.right
            if nd.val < prev.val:
                prev.left = nd
                
            else:
                prev.right = nd
            nd.parent = prev
    
    def nextmin(self,n):
        tmp = n.right
        while tmp.left is not None:
            tmp = tmp.left
        return tmp
    
    def transplant(self, u, v):
        if self.root == u:
            self.root = v
            v.parent = None
        else:
            if u.parent.left == u:
                u.parent.left = v
            else:
                u.parent.right = v
            v.parent = u.parent
    
    def delete(self,val):
        tmp = self.root
        while(tmp is not None and tmp.val != val):
            if val < tmp.val:
                tmp = tmp.left
            else:
                tmp = tmp.right
        
        if tmp.left is None:
            self.transplant(tmp,tmp.right)
        elif tmp.right is None:
            self.transplant(tmp, tmp.left)
        else:
            nmin = self.nextmin(tmp)
            if tmp.right != nmin:
                self.transplant(nmin,nmin.right)
                nmin.right = tmp.right
                nmin.right.parent = nmin
            nmin.left = tmp.left
            nmin.left.parent = nmin
            self.transplant(tmp,nmin)
            
            
if __name__ == "__main__":
    t = BST_P()

    nodes = [5,2,8,1,4,6,9,7]

    for i in nodes:
        t.insert(NodeP(i))
    t.delete(2)            
