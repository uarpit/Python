#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 11:00:43 2020
Queue with list
@author: arpit
"""

class Queue:
    def __init__(self,s):
        self.size = s
        self.q = ['']*s
        self.tail = 0
        self.head = -1
        
    def is_empty(self):
        return self.head == -1
    
    def is_full(self):
        return self.head == self.tail + 1
    
    def enqueue(self,val):
        if self.is_full():
            print("Queue is full")
        else:
            self.q[self.tail] = val
            if(self.tail == self.size-1):
                self.tail = 0
            else:
                self.tail += 1
            if self.head == -1:
                self.head = 0
            
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            tmp = self.q[self.head]
            self.head = (self.head + 1) % self.size
            if self.head == self.tail:
                self.head = -1
            return tmp
        
    def printq(self):
        tmp = self.head
        print("H", end= '->')
        while(tmp != self.tail):
            print(self.q[tmp], end = '->')
            tmp = (tmp + 1) % self.size
        #print(self.q[tmp],end = '->')
        print("T")
        
if __name__ == "__main__":
    q = Queue(5)
    q.enqueue(5)
    q.enqueue(10)
    q.printq()
    q.dequeue()
    q.enqueue(11)
    q.printq()
    q.enqueue(12)
    q.enqueue(13)
    q.enqueue(2)
    #q.remove()
    #q.remove()
    
    q.printq()
            
            