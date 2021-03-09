#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 23:38:48 2020
Given two strings write a method to determine if one is permutation of another
@author: arpit
"""
def check_perm(ip1,ip2):
    """
    This method uses dictionary to check count of each character 
    and then empties the dictionry while comparing the second string 
    """
    dict_char = {}
    
    for i in ip1:
        if i not in dict_char:
            dict_char[i] = 1
        else:
            dict_char[i] +=1
            
    for i in ip2:
        if i not in dict_char:
            return False
        elif dict_char[i] == 1:
            del dict_char[i]
        else:
            dict_char[i] -= 1
            
    return dict_char == {}

print(check_perm('abbe ', 'ba be'))