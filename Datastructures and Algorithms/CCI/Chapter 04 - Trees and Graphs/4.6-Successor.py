#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 15:30:12 2020
Write an algorithm to find the next node (in-order successor)
The node has a parent link
@author: arpit
"""
from BST_P import BST_P, NodeP

class BST_P_succ(BST_P):
    def successor(self,val):
        nd = self.root
        while nd.val != val:
            if val < nd.val:
                nd = nd.left
            else:
                nd = nd.right
                
        if nd.right is not None:
            return nd.right
        elif nd.parent is not None:
            if nd.parent.left == nd:
                return nd.parent
            elif nd.parent.parent is not None:
                while nd.parent.parent.right == nd.parent:
                    nd = nd.parent
                if nd.parent.parent.left == nd.parent:
                    return nd.parent.parent
                else: # nd.parent.parent == self.root:
                    return None
        else:
            return None

if __name__ == "__main__":
    t = BST_P_succ()

    nodes = [5,2,8,1,4,6,9,7]

    for i in nodes:
        t.insert(NodeP(i))
    #t.delete(2)         
    for i in nodes:
        try:
            result = t.successor(i).val
        except:
            result = None
        print(i,result)