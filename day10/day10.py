# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 15:24:54 2022

@author: Ashish
"""

instructions=[ line for line in open('day10_input.txt').read().split('\n')]
X=1
Xlist=[0]*241
cycle=0
totalStr=0

for line in instructions:
    if line =="noop":
        for _ in range(1):
            cycle+=1
            if cycle in [20,60,100,140,180,220]:
                # print(cycle,X)
                sigStr=cycle*X
                totalStr=sigStr+totalStr
            Xlist[cycle]=X
            print(cycle,X)
    else:
        for _ in range(2):
            cycle+=1    
            if cycle in [20,60,100,140,180,220]:
                
                sigStr=cycle*X
                totalStr=sigStr+totalStr
            Xlist[cycle]=X
            print(cycle,X)
        X=int(line.split(' ')[1]) + X

print("Part1",totalStr)

Xlist.pop(0)
Xlist.append(X)
ans = [[None] * 40 for _ in range(6)]

for row in range(6):
    for col in range(40):
        counter = row * 40 + col + 1
        if abs(Xlist[counter - 1] - (col)) <= 1:
            ans[row][col] = "##"
        else:
            ans[row][col] = "  "

# part 2
for row in ans:
    print("".join(row))
