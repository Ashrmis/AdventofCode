# -*- coding: utf-8 -*-

lines=[ line.strip() for line in open('day2_input.txt')]

# points dictionary
pts={('A','X'):4,('B','X'):1,('C','X'):7,
      ('A','Y'):8,('B','Y'):5,('C','Y'):2,
      ('A','Z'):3,('B','Z'):9,('C','Z'):6}

# part 2, X means lose, Y means draw, Z means win
pts2={('A','X'):3,('B','X'):1,('C','X'):2,
      ('A','Y'):4,('B','Y'):5,('C','Y'):6,
      ('A','Z'):8,('B','Z'):9,('C','Z'):7}


total_score1=0
total_score2=0
for r in lines:
    [opp,you]=r.split()
    total_score1=total_score1+pts[opp,you]
    total_score2=total_score2+pts2[opp,you]
print('total score part 1: ',total_score1)  
print('total score part 2: ',total_score2)        

