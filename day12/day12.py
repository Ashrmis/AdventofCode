from collections import deque
grid = [list(x) for x in open('day12.txt').read().strip().splitlines()]

# get start and end coordinates
for row in range(len(grid)):
    for col in range(len(grid[row])):
        if grid[row][col]=="S":
            startR,startC=[row,col]
            grid[row][col]="a"
        elif grid[row][col]=="E":
            endR,endC=[row,col]
            grid[row][col]="z"
# queue
q = deque()
q.append((0, startR, startC))

visted = {(startR, startC)}

while q:
    flag=False
    dist, r, c = q.popleft()
    for nextr, nextc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
        if nextr < 0 or nextc < 0 or nextr >= len(grid) or nextc >= len(grid[0]):
            continue
        if (nextr, nextc) in visted:
            continue
        if ord(grid[nextr][nextc]) - ord(grid[r][c]) > 1:
            continue
        if nextr == endR and nextc == endC:
            print("p1 ", dist + 1)
            flag=True
            break

        visted.add((nextr, nextc))
        q.append((dist + 1, nextr, nextc))
    
    if flag:
        break
    
    
# part 2  start at any a and go to end. Find shortest length.
# start backwards

# get start and end coordinates
for row in range(len(grid)):
    for col in range(len(grid[row])):
        if grid[row][col]=="S":
            grid[row][col]="a"
        elif grid[row][col]=="E":
            endR,endC=[row,col]
            grid[row][col]="z"
# queue
q = deque()
q.append((0, endR, endC))

visted = {(endR, endC)}

while q:
    flag=False
    dist, r, c = q.popleft()
    for nextr, nextc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
        if nextr < 0 or nextc < 0 or nextr >= len(grid) or nextc >= len(grid[0]):
            continue
        if (nextr, nextc) in visted:
            continue
        if ord(grid[nextr][nextc]) - ord(grid[r][c]) < -1:
            continue
        if grid[nextr][nextc]=='a':
            print("p2 ", dist + 1)
            flag=True
            break

        visted.add((nextr, nextc))
        q.append((dist + 1, nextr, nextc))
    
    if flag:
        break
