#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 05:30:17 2020
Reverse a singly linked list without recursion
@author: arpit
"""
from SinglyLinkedList import SLL,Node

def rev_ll(ll):
    prev = ll.head
    if ll.head.next is not None:
        ptr = ll.head.next
        prev.next = None
        while(ptr.next is not None):
            tmp = ptr
            ptr = ptr.next
            tmp.next = prev
            prev = tmp
        ptr.next = prev
        ll.head = ptr            
    return ll.head
    
    
    while(ptr.next is not None):
        tmp = ptr
        ptr = ptr.next
        ptr.next.next = prev

if __name__ == "__main__":
    ll = SLL()
    ll.insert(5)
    #ll.insert(10)
    #ll.insert(6)
    ll.printll()
    rev_ll(ll)
    ll.printll()

