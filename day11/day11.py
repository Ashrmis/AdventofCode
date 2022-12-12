monkeys=[]

def grp_monkeys():
    for group in open('day11_input.txt').read().strip().split("\n\n"):
        monkey = []
        lines = group.split('\n')
        
        monkey.append(list(map(int, lines[1].split(": ")[1].split(", "))))
        monkey.append(eval("lambda old:" + lines[2].split("=")[1]))
        
        monkey.append(int(lines[3].split()[-1]))
        monkey.append(int(lines[4].split()[-1]))
        monkey.append(int(lines[5].split()[-1])) 
        
        monkeys.append(monkey)
    return monkeys
    
def part1(monkeys):
    passes=[0]*len(monkeys)
    for _ in range(20):
        for index,mk in enumerate(monkeys):
            passes[index]=passes[index]+len(mk[0])
            for item in mk[0]:
                item=mk[1](item)
                item=item//3
                if item % mk[2] ==0:
                    monkeys[mk[3]][0].append(item)
                    
                    
                else:
                    monkeys[mk[4]][0].append(item)
            mk[0]=[] # empty out the item after each monkey
            
    passes.sort()
    print(passes[-1]*passes[-2])
    

def part2(monkeys):
    mod = 1
    for monkey in monkeys:
        mod *= monkey[2]
    counts=[0]*len(monkeys)
    for _ in range(10000):
        for index, monkey in enumerate(monkeys):
            for item in monkey[0]:
                item = monkey[1](item)
                item %= mod
                if item % monkey[2] == 0:
                    monkeys[monkey[3]][0].append(item)
                else:
                    monkeys[monkey[4]][0].append(item)
            counts[index] += len(monkey[0])
            monkey[0] = []
        
    
    counts.sort()
    print(counts[-1] * counts[-2])
    
part1(grp_monkeys())

part2(grp_monkeys())



