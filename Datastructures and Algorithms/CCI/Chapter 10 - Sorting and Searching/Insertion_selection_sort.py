#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 04:26:24 2020
Insertion sort
Selection sort
@author: arpit
"""
def ins_sort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j=i
        while( j > 0 and key < arr[j-1]):
            arr[j] = arr[j-1]
            j-=1
        arr[j] = key
        
def sel_sort(arr):
    for i in range(1,len(arr)):
        mini = i-1
        for j in range(i,len(arr)):
            if arr[j] < arr[mini]:
                mini = j
        arr[i-1],arr[mini] = arr[mini],arr[i-1]
    
    
    
    
input1 = [1,5,2,7,4]
input2 = [1,5,2,7,4]
#input2 = [1]
ins_sort(input1)
print(input1)
sel_sort(input2)
print(input2)
    
