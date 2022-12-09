# -*- coding: utf-8 -*-

import numpy as np
grid = [list(map(int, line)) for line in open('test.txt').read().splitlines()]
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


# part 2 332640



