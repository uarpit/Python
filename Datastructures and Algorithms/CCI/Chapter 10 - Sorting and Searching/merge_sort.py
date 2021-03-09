#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 19:20:33 2020
Merge sort
@author: arpit
"""

def merge_sort(arr,p,q):
    if p==q:
        return
    else:
        mid = int((p+q)/2)
        #print(p,mid,q)
        merge_sort(arr,p,mid)
        merge_sort(arr,mid+1,q)
        merge(arr,p,mid,q)

def merge(arr,p,mid,q):
    n1 = mid - p + 1
    n2 = q - mid
    l1 = []
    l2 = []
    
    for i in range(0,n1):
        l1.append(arr[p+i])
    l1.append(float('inf'))
    for j in range(0,n2):
        l2.append(arr[mid+1+j])
    l2.append(float('inf'))

    i=0
    j=0
    for k in range(p,q+1):
        if l1[i]<=l2[j]:
            arr[k] = l1[i]
            i += 1
        else:
            arr[k] = l2[j]
            j += 1
            
if __name__ == "__main__":
    arr = [6,2,4,9,10,5,7,1]
    print(arr)
    merge_sort(arr,0,len(arr)-1)
    print(arr)