#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 18:34:41 2020
Symmetric Tree: Given a binary tree, check whether it is a mirror of itself
@author: arpit
"""

from BT import BT,Node
from collections import deque

class Solution:
    def isSymmetric(self, root):
        if root is not None:
            r1 = root.left
            r2 = root.right
            #return self.check( r1, r2)
            return self.check_iter(root)
        else:
            return True
        
    def check(self,p,q):
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        return p.val == q.val and (self.check(p.left,q.right) and self.check(p.right, q.left))
        
    def check_iter(self,root):
        dq = deque()
        dq.append(root)
        dq.append(root)
        while len(dq) > 0:
            x = dq.popleft()
            y = dq.popleft()
            if x is None and y is None:
                continue
            elif x is None or y is None:
                return False
            elif x.val != y.val:
                return False
            else:
                dq.append(x.right)
                dq.append(y.left)
                dq.append(x.left)
                dq.append(y.right)
        return True
            
if __name__ == "__main__":
    t = BT()

    nodes = [1,2,2,None,3,None,3]

    for x,i in enumerate(nodes):
        if x == 0:
            r = Node(i)
            t.insert(r)
        else:
            t.insert(Node(i))
    s = Solution()
    print(s.isSymmetric(r))
    
    
    