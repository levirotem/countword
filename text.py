
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 16:40:23 2021

@author: levir
"""


def revword(word:str) -> str:

    i=len(word)
    new_str= ""
    while i:
        i =i-1
        new_str = new_str + word[i]

    return new_str.lower()



def countword()->int:

    
    file= open('text.txt')
    first_line = file.readline()
    count=0
    for line in file:
        line=line.rsplit()
        
    
        for word in line:
            
            word= revword(word)
            
            if  word in first_line:
                count= count+1
    return(count)

    
            
            
            
            
            
            