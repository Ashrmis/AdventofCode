# -*- coding: utf-8 -*-

import numpy as np
grid = [list(map(int, line)) for line in open('day8_input.txt').read().splitlines()]
gridarr=np.array(grid)

tree_coordinates={}
edge={}
trees=0


for r in range(gridarr.shape[0]):
    for c in range(gridarr.shape[1]):
        curr_h=gridarr[r,c]
        if (gridarr.shape[0]-1>r>=1 and gridarr.shape[1]-1>c>=1):
            if all(curr_h > x for x in gridarr[r,c+1:]) or all(curr_h > x for x in gridarr[r,:c]):
                tree_coordinates[(r+1,c+1)]=(gridarr[r,c],"INTERIOR")
            if all(curr_h > x for x in gridarr[:r,c]) or all(curr_h > x for x in gridarr[r:,c]):
                tree_coordinates[(r+1,c+1)]=(gridarr[r,c],"INTERIOR")


        else: # edges
            tree_coordinates[(r,c)]=(gridarr[r,c],"EDGE")
    

print(len(tree_coordinates))

# part 1 1859
# part 2 332640