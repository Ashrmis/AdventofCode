from collections import defaultdict

data = open("day7_input.txt").read().strip()
lines = [x for x in data.split('\n')]

# SZ is the path with all files and sub-directories
SZ = defaultdict(int)
path = []
for line in lines:
    words = line.strip().split()
    if words[1] == 'cd':
        if words[2] == '..':
            path.pop()
        else:
            path.append(words[2])
    elif words[1] == 'ls': # don't do anything if ls
        continue
    elif words[0] == 'dir': # don't do anything if dir
        continue
    else:
        sz = int(words[0]) # else means it's a file, get that size
        # Add this file's size to the current directory size *and* the size of all parents
        for i in range(1, len(path)+1):
            SZ['/'.join(path[:i])] += sz


part1=0

# arbitrary large number
part2=100000000000000000

max_allowed=40000000
total_used=SZ['/']
need_to_free=total_used-max_allowed



for keys,value in SZ.items():
    if value<=100000:
       part1+=value
    if value >=need_to_free:
        part2=min(part2,value)

print(part1,part2)