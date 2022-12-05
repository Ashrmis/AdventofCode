 # -*- coding: utf-8 -*-
"""
Day 1 advent of code
"""


lines=[ line.strip() for line in open('day1_input.txt')]

lines_mod='\n'.join(lines).split('\n\n')
elf_totals=[]
for l in lines_mod:
    chunk_total=0
    for i in l.split("\n"):
        chunk_total=int(i)+chunk_total
    elf_totals.append(chunk_total)
print("Part 1 Most calories: ",max(elf_totals))

print("Part 2 Top 3 calories :",sum(sorted(elf_totals,reverse=True)[0:3]))


