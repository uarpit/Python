#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 19:36:43 2022

Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.
A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

@author: arpit
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        if root is None:
            return False
        else:
            if self.isSame(root,subRoot):
                return True
            return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
    
    def isSame(self,p,q):
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        else:
            if p.val != q.val:
                return False
            else:
                return self.isSame(p.left,q.left) and self.isSame(p.right,q.right)