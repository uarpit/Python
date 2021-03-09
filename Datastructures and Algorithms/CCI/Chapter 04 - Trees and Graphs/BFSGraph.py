#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 16:28:13 2020
Program for Breadth First Search implementation
@author: arpit
"""
from collections import defaultdict,deque

class Node:
    def __init__(self, val):
        self.val = val
        self.parent = None
        self.dist = None
        self.color = 'White'

class Graph:
    
    def __init__(self):
        #dictionary of values and adjecent nodes
        self.V = set([])
        self.edges = defaultdict(set) #Default empty set for each vertex value
    
    def add_edge(self,u,v):
        self.V.add(u)
        self.V.add(v)
        self.edges[u.val].add(v)
        #self.edges[v.val].add(u) # add this for bidirectional graph
    
    def BFS(self,s,e=None): #s = start and e = end node
        q=deque()
        s.color = 'Grey'
        s.dist = 0
        q.append(s)
        while q:
            i = q.popleft()
            for j in self.edges[i.val]:
                if j.color == 'White':
                    j.color = 'Grey'
                    j.parent = i
                    j.dist = i.dist + 1
                    q.append(j)
            i.color = 'Black'
            print(i.val, "distance is {}".format(i.dist))
            if i == e:
                return True
        return False
        
if __name__ == "__main__":
    g = Graph()
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    g.add_edge(a, b)
    g.add_edge(a, c)
    g.add_edge(d, c)
    print(g.BFS(a,c))
        
        
        
    