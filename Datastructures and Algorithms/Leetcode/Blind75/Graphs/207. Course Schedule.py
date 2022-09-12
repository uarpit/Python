#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 20:16:28 2022

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
    For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

@author: arpit
"""
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        #build depedency graph
        dependency_dict = {i:[] for i in range(numCourses)}
        for i in prerequisites:
            dependency_dict[i[0]].append(i[1])
        
        visit_set = set()
        
        def dfs(course):
            if course in visit_set:
                return False
            if dependency_dict[course] == []:
                return True
            else:
                visit_set.add(course)
                for i in dependency_dict[course]:
                    if not dfs(i):
                        return False
                visit_set.remove(course)
                dependency_dict[course] = []
                return True
        
        for i in range(numCourses):
            if not dfs(i): return False
        return True