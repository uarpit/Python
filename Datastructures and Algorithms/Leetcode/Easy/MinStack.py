#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 17:07:20 2020
Design a stack that supports push, pop, top, and 
retrieving the minimum element in constant time.

    push(x) -- Push element x onto stack.
    pop() -- Removes the element on top of the stack.
    top() -- Get the top element.
    getMin() -- Retrieve the minimum element in the stack.

@author: arpit
"""
class Node:
    def __init__(self,val):
        self.val = val
        self.minv = None
        self.next = None
    
    def set_min(self, x):
        if x < self.val:
            self.minv = x
        else:
            self.minv = self.val

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.head = None

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        n = Node(x)
        if self.head is None:
            n.set_min(x)
        else:
            n.set_min(self.head.minv)
            n.next = self.head
        self.head = n


    def pop(self):
        """
        :rtype: None
        """
        if self.head is None:
            print("Stack is empty")
        else:
            self.head = self.head.next

    def top(self):
        """
        :rtype: int
        """
        return self.head.val

    def getMin(self):
        """
        :rtype: int
        """
        return self.head.minv


if __name__ == "__main__":
    minStack = MinStack();
    minStack.push(-2);
    minStack.push(0);
    minStack.push(-3);
    print(minStack.getMin()); # return -3
    minStack.pop();
    print(minStack.top());    # return 0
    print(minStack.getMin()); # return -2
