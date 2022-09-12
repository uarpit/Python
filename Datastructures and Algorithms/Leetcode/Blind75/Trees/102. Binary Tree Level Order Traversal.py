#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 19:36:07 2022

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

@author: arpit
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        if root is None:
            return
        else:
            q = deque()
            q.append(root)
            d =1
            while q:
                out = []
                for i in list(q):
                    n = q.popleft()
                    out.append(n.val)
                    if n.left:
                        q.append(n.left)
                    if n.right:
                        q.append(n.right)
                d += 1
                result.append(out)
        return result