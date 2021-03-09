#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 18:01:50 2020
Robot sitting on upper left coner of grid with r rows and c columns. 
It can move only right and down. Certain cells are off limits.
Find path for robot from top left to bottom right
@author: arpit
"""

class GridPath:
    
    def __init__(self, size):
        self.size = size
        self.failedpoints = set({})
        self.path = []
        # This wont work if you want to change a single element in future
        # As it resuses list object and changing one element will result 
        # in changing all the elements in that column
        #self.grid = [[-1]*size]*size 
        self.grid = [[-1 for i in range(0,size)] for j in range(0,size)]
        self.closed = [[1,1], [2,1], [0,3]]
        
        for r,c in self.closed:
            self.grid[r][c] = 0


    def print_grid(self):
        for r,row in enumerate(self.grid):
            for c,col in enumerate(row):
                print(self.grid[r][c], end=(" "))
            print("")
    
    def getpath(self, r, c):
        if r < 0 or c < 0:
            return False
        if self.grid[r][c] == 0:
            return False
        if (r,c) in self.failedpoints:
            return False
        is_origin = ((r == 0) and (c == 0))
        
        if(is_origin or self.getpath(r-1,c) or self.getpath(r,c-1)):
            self.path.append([r,c])
            return True
        
        self.failedpoints.add((r,c))
        return False


if __name__ == "__main__":
    g = GridPath(5)
    g.print_grid()
    g.getpath(4,4)
    print(g.path)