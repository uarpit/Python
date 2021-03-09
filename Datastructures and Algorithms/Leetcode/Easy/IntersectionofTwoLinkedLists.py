#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 14:40:12 2020

@author: arpit
"""
from SinglyLinkedList import SLL,Node

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        stk1 = []
        ptr = headA
        while ptr is not None:
            stk1.append(ptr)
            ptr = ptr.next
        stk2 = []
        ptr = headB
        while ptr is not None:
            stk2.append(ptr)
            ptr = ptr.next
        prev = None
        while len(stk1) > 0 and len(stk2) > 0:
            p = stk1.pop()
            q = stk2.pop()
            if p != q:
                return prev
            prev = p
            
        return prev
    
    def getIntersectionNode_2(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        len1 = 0
        ptr = headA
        while ptr is not None:
            len1 += 1
            ptr = ptr.next
        len2 = 0
        ptr = headB
        while ptr is not None:
            len2 += 1
            ptr = ptr.next    
        if len2 > len1:
            ptr = headB
            ptr2 = headA
            for i in range(0,len2-len1):
                ptr = ptr.next
        else:
            ptr = headA
            ptr2 = headB
            while ptr is not None:
                if ptr == ptr2:
                    return ptr
                else:
                    ptr = ptr.next
                    ptr2 = ptr2.next
                    
            
            
                
        
    
if __name__ == "__main__":
    ll1 = SLL()
    head1 = Node(4)
    n1 = Node(8)
    n2 = Node(4)
    n3 = Node(5)
    ll1.insert(n1)
    ll1.insert(n2)
    ll1.insert(n3)
    nd = Node(1)
    ll1.insert(nd)
    ll1.insert(head1)
    
    
    ll2 = SLL()
    ll2.insert(n1)
    ll2.insert(n2)
    ll2.insert(n3)
    head2 = Node(7)
    
    nd = Node(6)
    ll2.insert(nd)
    nd = Node(1)
    ll2.insert(nd)
    ll2.insert(head2)
    ll1.printll()
    ll2.printll()
    s = Solution()
    #print(head1.val,head2.val)
    #for i in ll1:
    #    print(i.val, end = '->')
    print(s.getIntersectionNode(head1,head2).val)
    