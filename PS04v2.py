# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 15:49:58 2019

@author: user
"""

import os
import re

os.chdir("C:\\Users\\user\\Documents\\IMT511\\PS4")
def language(filename):
    with open (filename, encoding = "utf-8") as file_object:
        contents = file_object.read()
    s = contents.split()
    List = []
    for word in s:
        x = word.lower().strip ("|©!@#$%^&*()-_=+,.;:?/<>'`[]''")
        List.append(x)
    #print(List)
    
    counts = {}
    for word in List:
        if not word in counts:
            counts[word] =0
        counts[word] += 1
    #print(counts)
    sorted_counts = sorted (counts.items(), key = lambda kv: kv[1], reverse = True)
    
    most_frequent = dict(sorted_counts[:11])
    
    for word in most_frequent.keys():
        most_frequent[word] = most_frequent[word]/len(sorted_counts)
        
    return(most_frequent)

spanish = (language('cherbonnel-mi-tio_SP.txt'))
english = (language('eaton-boy-scouts_EN.txt'))
german = (language('schloemp-tolle-koffer_DE.txt'))
unknown = (language('unknown-lang.txt'))

for u in unknown.keys():
    s = spanish.get(u, 0)
    u = unknown.get(u, 0)
    spanish_difference = abs(s-u)
    
    g = german.get(u, 0)
    german_difference = abs(g-u)
    
    e = english.get(u, 0)
    english_difference = abs(e-u)
print("The difference between Spanish is: ", spanish_difference)
print("The difference between German is: ", german_difference)
print("The difference between English is: ", english_difference)    


