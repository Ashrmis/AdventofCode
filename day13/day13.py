x = list(map(str.splitlines, open('day13.txt').read().strip().split("\n\n")))

def compare(x, y):
    if type(x) == int:
        if type(y) == int:
            return x - y
        else:
            return compare([x], y)
    else:
        if type(y) == int:
            return compare(x, [y])
    
    for a, b in zip(x, y):
        v = compare(a, b)
        if v:
            return v
    
    return len(x) - len(y)

pairs = 0

for i, (l, r) in enumerate(x):
    if compare(eval(l), eval(r)) < 0:
        pairs = pairs + (i+1)

print(pairs)
    
        
# part 2

