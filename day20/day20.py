# linked list :)
class Node:
    def __init__(self, n):
        self.n = n
        self.left = ""
        self.right = ""

x = [Node(int(x)) for x in open('day20.txt')]
# for part 2
# x = [Node(811589153*int(x)) for x in open('day20.txt')]

# get the left and rights of each item
for i in range(len(x)):
    x[i].right = x[(i + 1) % len(x)]
    x[i].left = x[(i - 1) % len(x)]

mod = len(x) - 1

# mixing
# move and rearrange the new lefts and rights
# for _ in range(10): # for part 2
for a in x:
    if a.n == 0:
        zloc = a
        continue
    curr_a = a
    if a.n > 0:
        for _ in range(a.n % mod):
            curr_a = curr_a.right
            
        if a == curr_a:
            continue
        
        a.right.left = a.left
        a.left.right = a.right
        curr_a.right.left = a
        a.right = curr_a.right
        curr_a.right = a
        a.left = curr_a
    # left. flip the lefts to rights, and rights to lefts
    else:
        for _ in range(a.n % mod):
            curr_a = curr_a.left
            
        if a == curr_a:
            continue
        
        a.left.right = a.right
        a.right.left = a.left
        curr_a.left.right = a
        a.left = curr_a.left
        curr_a.left = a
        a.right = curr_a

total = 0

# every 1000, add to total
for _ in range(3):
    for _ in range(1000):
        zloc = zloc.right
    total =total+ zloc.n

print(t)
