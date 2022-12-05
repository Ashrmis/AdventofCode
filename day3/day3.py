# -*- coding: utf-8 -*-

def get_score(letter):
    if letter.isupper():
        score=ord(letter)-38
    if letter.islower():
        score=ord(letter)-96
        
    return score

lines=[ line.strip() for line in open('day3_input.txt')]
score=0
for rs in lines:
    c1=rs[0:(len(rs)//2)]
    c2=rs[(len(rs)//2):len(rs)]
    
    for letter in c1:
        if letter in c2:
            score=score+get_score(letter)
            break;
            
print(score)
# part 2, every 3 lines is a group, find common letter in 3 groups
score=0
i=0
while i < len(lines):
    for letter in lines[i]:
        
        if letter in lines[i+1] and letter in lines[i+2]:
            score=score+get_score(letter)
            
            break;
    i=i+3
    
    
print(score)
