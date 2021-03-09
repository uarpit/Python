#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 19:57:17 2020
Singly Linked list implementation
Insert at head
Search and remove the node
@author: arpit
"""

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        
class SLL:
    def __init__(self):
        self.head = None
        
    def insert(self,val):
        nd = Node(val)
        nd.next = self.head
        self.head = nd
        
    def is_empty(self):
        return self.head is None
    
    def remove(self, val):
        if self.is_empty():
            print("Error: List is already empty")
        else:
            if self.head.val == val:
                self.head = self.head.next
                print("Removed {}".format(val))
            else:
                ptr = self.head
                while(ptr.next is not None):
                    if ptr.next.val == val:
                        ptr.next = ptr.next.next
                        print("Removed {}".format(val))
                        break
                    ptr = ptr.next
                else:
                    print("{} not found".format(val))
        
    def __iter__(self):
        ptr = self.head
        while(ptr is not None):
            yield ptr
            ptr = ptr.next
    
    def printll(self):
        ptr = self.head
        while(ptr.next is not None):
            print(ptr.val,end = '->' )
            ptr = ptr.next
        print(ptr.val)
        
if __name__ == "__main__":
    ll = SLL()
    ll.insert(5)
    ll.insert(10)
    ll.insert(6)
    #ll.remove(10)
    #ll.remove(5)
    #ll.remove(6)
    #ll.remove(8)
    #ll.printll()
    for i in ll:
        print(i.val)
    
        
