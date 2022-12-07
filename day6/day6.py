# -*- coding: utf-8 -*-
line=[ line.strip() for line in open('day6_input.txt')][0]

def get_marker(numChar: int) -> int:
    for i in range(len(line)):
        if len(set(line[i:i+numChar])) ==numChar:
            ans=i+numChar
            break;
    return ans

print(get_marker(4))
print(get_marker(14))