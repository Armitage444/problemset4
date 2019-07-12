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
        most_frequent[word] = most_frequent[word]/len(List)
        
    return(most_frequent)

spanish = (language('cherbonnel-mi-tio_SP.txt'))
english = (language('eaton-boy-scouts_EN.txt'))
german = (language('schloemp-tolle-koffer_DE.txt'))
unknown = (language('unknown-lang.txt'))

sum_german = 0
for w in unknown.keys():
    g = abs(german.get(w,0) - unknown.get(w))
    sum_german = sum_german + g
    
sum_english = 0
for w in unknown.keys():
    e = abs(english.get(w,0) - unknown.get(w))
    sum_english = sum_english + e
    
sum_spanish = 0
for w in unknown.keys():
    s = abs(spanish.get(w,0) - unknown.get(w))
    sum_spanish = sum_spanish + s
    
print("The difference between German is: ", sum_german)
print("The difference between English is: ", sum_english)
print("The difference between Spanish is: ", sum_spanish)

if sum_spanish < sum_english and sum_spanish < sum_german:
    print("This text is in Spanish")
elif sum_german < sum_english and sum_german < sum_spanish:
    print("This text is in German")
else:
    print("This text is in English")
