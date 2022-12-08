# -*- coding: utf-8 -*-
commands=[ line.strip() for line in open('test.txt')]
cmds=[]
for x in range(len(commands)):
    if "cd" in commands[x]:
        cmds.append(commands[x])
    try:
        test=int(commands[x][0])
    except ValueError:
        test=""
    if type(test) == int:
        cmds.append(commands[x])

test=[]
for a in cmds:
    if not ".." in a:
       test.append(a) 
found=0
for b in range(len(test)):
    if "cd" in test[b]:
       found+=1
       if found == 2:
           start=b
           break
total=0
storage=[]
s=[]
for c in range(start,len(test)):
    if 'cd' in test[c]:
        s.append((storage))
        total=0
        tmp=[]
        storage=[]
    else:
        tmp=int(test[c].split(" ")[0])
        
        storage.append(tmp)
    if c+1 == len(test):
        s.append((storage))
        
        
        
# total=0
# for x in s:
#     if x<=100000:
#         print(x,total)
#         total=x+total
