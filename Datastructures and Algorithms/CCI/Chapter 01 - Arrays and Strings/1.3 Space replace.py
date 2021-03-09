#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 23:40:14 2020
Replace space with %20, assuming that there are enough spaces in the array 
@author: arpit
"""
def str_replc(ip, arr_size):
    """
    Implementing this using lists
    """
    tail = arr_size-1
    ip_lst = list(ip)
    for i in range(tail,-1,-1):
        if ip_lst[i] != ' ':
            head = i
            break
        else:
            continue
            
    for i in range(head,-1,-1):
        if ip_lst[i] != ' ':
            ip_lst[tail] = ip_lst[i]
            tail -= 1
        else:
            ip_lst[tail] = '0'; tail -=1
            ip_lst[tail] = '2'; tail -=1
            ip_lst[tail] = '%'; tail -=1
    
    return ''.join(ip_lst)

print(str_replc("Hi this is a test        ", 25))
