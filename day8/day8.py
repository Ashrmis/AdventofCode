# -*- coding: utf-8 -*-

import numpy as np
grid = [list(map(int, line)) for line in open('day8_input.txt').read().splitlines()]
gridarr=np.array(grid)

tree_coordinates={}


for r in range(gridarr.shape[0]):
    for c in range(gridarr.shape[1]):
        curr_h=gridarr[r,c]
        # if current tree isn't an edge tree
        if (gridarr.shape[0]-1>r>=1 and gridarr.shape[1]-1>c>=1):
          
            # check left and right of the current tree
            if all(curr_h > x for x in gridarr[r,c+1:]) or all(curr_h > x for x in gridarr[r,:c]):
                tree_coordinates[(r+1,c+1)]=(gridarr[r,c],"INTERIOR")
              
                # check top and bottom of the current tree
            if all(curr_h > x for x in gridarr[:r,c]) or all(curr_h > x for x in gridarr[r+1:,c]):
                tree_coordinates[(r+1,c+1)]=(gridarr[r,c],"INTERIOR")
            
     
            
           
edge_count=4*(gridarr.shape[0]-1)

print("Part 1",len(tree_coordinates)+edge_count)



p2_scores=[]
for r in range(gridarr.shape[0]):
    for c in range(gridarr.shape[1]):
        curr_h=gridarr[r,c]
        # if current tree isn't an edge tree
        if (gridarr.shape[0]-1>r>=1 and gridarr.shape[1]-1>c>=1):
            Lscore,Rscore,Uscore,Dscore=0,0,0,0
            
            #down
            for x in range(len(gridarr[r+1:,c])):
                if curr_h > gridarr[r+1:,c][x]:
                    Dscore=Dscore+1
                elif curr_h == gridarr[r+1:,c][x]:
                    Dscore=x+1
                    break
                elif curr_h < gridarr[r+1:,c][x]:
                    if Dscore==0:
                        Dscore=0
                    else:
                        Dscore=Dscore+1
                    break
            #up
            for x in range(len(gridarr[:r,c])):
                if curr_h > gridarr[:r,c][x]:
                    Uscore=Uscore+1
                elif curr_h == gridarr[:r,c][x]:
                    Uscore=x+1
                    break
                elif curr_h < gridarr[:r,c][x]:
                    if Uscore==0:
                        Uscore=0
                    else:
                        Uscore=Uscore+1
                    break
            #right
            for x in range(len(gridarr[r,c+1:])):
                if curr_h > gridarr[r,c+1:][x]:
                    Rscore=Rscore+1
                elif curr_h == gridarr[r,c+1:][x]:
                    Rscore=x+1
                    break
                elif curr_h < gridarr[r,c+1:][x]:
                    if Rscore==0:
                        Rscore=0
                    else:
                        Rscore=Rscore+1
                    break
            #left
            for x in range(len(gridarr[r,:c])):
                if curr_h > gridarr[r,:c][x]:
                    Lscore=Lscore+1
                elif curr_h == gridarr[r,:c][x]:
                    Lscore=x+1
                    break
                elif curr_h < gridarr[r,:c][x]:
                    if Lscore==0:
                        Lscore=0
                    else:
                        Lscore=Lscore+1
                    break

        if Uscore and Dscore and Lscore and Rscore > 0:
            p2_scores.append([Lscore,Rscore,Uscore,Dscore])


print("Part 2",np.prod(max(p2_scores)))


