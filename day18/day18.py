cubes = open("test.txt").read().strip().split("\n")

adj=0
cube_set=set()
for c in cubes:
    x,y,z=c.split(',')
    x=int(x)
    y=int(y)
    z=int(z)
    cube_set.add((x,y,z))

for c in cubes:
    x,y,z=c.split(',')
    x=int(x)
    y=int(y)
    z=int(z)
    
    # check x,y,z
    
    if (x+1,y,z) in cube_set:
        adj=adj+1
    if (x+1,y,z) in cube_set:
        adj=adj+1
        
    if (x,y+1,z) in cube_set:
        adj=adj+1
    if (x,y-1,z) in cube_set:
        adj=adj+1
        
    if (x,y,z+1) in cube_set:
        adj=adj+1
    if (x,y,z-1) in cube_set:
        adj=adj+1
    
        
print(len(cubes)*6 - adj)



