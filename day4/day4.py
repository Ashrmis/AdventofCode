# -*- coding: utf-8 -*-

lines=[ line.strip() for line in open('day4_input.txt')]
part1=0
part2=0
for pair in lines:
    p1,p2=pair.split(",")
    p1s,p1e=p1.split("-")
    p2s,p2e=p2.split("-")
    p1s,p2s,p1e,p2e = [int(x) for x in [p1s,p2s,p1e,p2e]]

    # in range
    if p1s <= p2s and p2e <= p1e or p2s <= p1s and p1e <= p2e:
        part1+=1

    # any overlap
    p1list=list(range(p1s,p1e+1))
    p2list=list(range(p2s,p2e+1))
    for x in p1list:
        if x in p2list:
            part2+=1
            break



print(part1)
print(part2)
