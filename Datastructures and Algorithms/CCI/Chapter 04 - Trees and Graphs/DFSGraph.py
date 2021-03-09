#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 23:10:16 2020
Implement Deapth First search graph
@author: arpit
"""
from collections import defaultdict

class Node:
    def __init__(self, val):
        self.val = val
        self.d = None #discovery time
        self.f = None #final visit time
        self.parent = None # link to ancestor
        self.color = 'White' # state of node (White = not visited; Grey = discovered and discovering adjacent nodes; Black = visit comlete)
        self.dist = 0 # distance from start node
        
class Graph:
    def __init__(self):
        self.V = set([])
        self.edges = defaultdict(set)
        self.time = 0
        
    def add_edge(self,u,v):
        self.V.add(u)
        self.V.add(v)
        self.edges[u.val].add(v)
        self.edges[v.val].add(u) # add this for bidirectional graph
        
    def DFS(self,s): #s = start and e = end node
        self.time += 1
        s.d = self.time
        s.color = 'Grey'
        
        for i in self.edges[s.val]:
            if i.color == 'White':
                i.parent = s
                i.dist = s.dist + 1
                self.DFS(i)
        self.time += 1
        s.f = self.time
        s.color = 'Black'
        print(s.val, "at discovery time {}, visit time {} and distance is {}".format(s.d,s.f,s.dist))

if __name__ == '__main__':
    g = Graph()
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    g.add_edge(a, b)
    g.add_edge(a, c)
    g.add_edge(d, c)
    g.DFS(a)