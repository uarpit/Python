#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 23:00:19 2020
Remove Duplicates from unsorted Linked list
@author: arpit
"""

from SinglyLinkedList import SLL,Node

def rem_dups(ll):
    track = set([])
    ptr = ll.head
    while(ptr is not None):
        prev = ptr
        if ptr.val in track:
            ptr = ptr.next
            prev.next = ptr
        else:
            track.add(ptr.val)
            ptr = ptr.next
        
        
        
if __name__ == "__main__":
    ll = SLL()
    ll.insert(5)
    ll.insert(10)
    ll.insert(6)
    ll.insert(10)
    ll.insert(5)
    ll.printll()
    rem_dups(ll)
    ll.printll()
