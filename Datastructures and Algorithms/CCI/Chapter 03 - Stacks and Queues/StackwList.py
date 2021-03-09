#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 10:04:56 2020
Stack usging List
@author: arpit
"""

class Stack:
    def __init__(self, s):
        self.top = -1
        self.size = s
        self.stk = ['']*self.size
        
    def is_full(self):
        return self.top +1 == self.size
    
    def is_empty(self):
        return self.top == -1
        
    def push(self, val):
        if self.is_full():
            print("Stack is already full")
        else:
            self.top += 1
            self.stk[self.top] = val
            
    def pop(self):
        if self.is_empty():
            print("Stack is already empty")
        else:
            tmp = self.stk[self.top]
            self.top -= 1
            return tmp
        
    def peek(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            return self.stk[self.top]
    
    def print_stk(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print("T", end = '->')
            tmp = self.top
            while(tmp > 0):
                print(self.stk[tmp], end = '->')
                tmp -= 1
            print(self.stk[tmp])
            
if __name__ == "__main__":
    stk = Stack(5)
    stk.push(5)
    stk.push(10)
    print(stk.pop())
    stk.push(11)
    stk.push(6)
    #stk.pop()
    #stk.pop()
    #stk.pop()
    stk.print_stk()
        