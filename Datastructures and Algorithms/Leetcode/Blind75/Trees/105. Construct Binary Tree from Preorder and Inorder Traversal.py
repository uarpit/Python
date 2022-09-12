#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 12:30:58 2022

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

@author: arpit
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder  or not inorder:
            return None
        else:
            root = TreeNode(preorder[0])
            mid = inorder.index(preorder[0])
            root.left = self.buildTree(preorder[1:mid+1],inorder[:mid+1])
            root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root