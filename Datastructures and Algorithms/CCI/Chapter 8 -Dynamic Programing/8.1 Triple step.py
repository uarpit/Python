#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 19:28:26 2020
Child is running up a stair case n steps and can hop either 1 step, 2 step 
or 3 steps. Possible ways the child can run up the stairs
@author: arpit
"""

class Stairs:
    def __init__(self,n):
        self.num_str = n
        self.cash = [-1]*(n+1)
    
    def run_ways(self):
        x = self.num_str   #While using it in cluster try to not send object variable
        return self.run(x) #This will avoid entire object being transmitted in cluster
                           

    def run(self,remng):
        if remng < 0:
            return 0
        elif remng == 0:
            return 1
        else:
            if self.cash[remng] != -1:
                return self.cash[remng]
            else:
                self.cash[remng] = self.run(remng-1) + self.run(remng-2) + self.run(remng-3)
                return self.cash[remng]

if __name__ == "__main__":
    s = Stairs(10)
    print(s.run_ways())