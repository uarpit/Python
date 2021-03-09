#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 09:03:10 2020
Given a directed graph write an algorith to see if there is a route
between the two nodes
@author: arpit
"""
from BFSGraph import Graph, Node

if __name__ == "__main__":
    g = Graph()
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    g.add_edge(a, b)
    g.add_edge(a, c)
    g.add_edge(d, c)
    if g.BFS(a,c):
        ptr = c
        print("Head",end="")
        while(ptr.parent is not None):
            print(" -> {}".format(ptr.val),end="")
            ptr = ptr.parent
        print(" -> {}".format(ptr.val),end="")
    else:
        print("The path doesnot exist")
            


