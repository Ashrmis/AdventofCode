# -*- coding: utf-8 -*-

lines=[ line.strip() for line in open('day5_input.txt')]

[config,moves]='\n'.join(lines).split('\n\n')

# wrote out the whole stacks rather than parsing and creating a list for it

stacks=[['[Q]','[S]','[W]','[C]','[Z]','[V]','[F]','[T]'],
        ['[Q]','[R]','[B]'],
        ['[B]','[Z]','[T]','[Q]','[P]','[M]','[S]'],
        ['[D]','[V]','[F]','[R]','[Q]','[H]'],
        ['[J]','[G]','[L]','[D]','[B]','[S]','[T]','[P]'],
        ['[W]','[R]','[T]','[Z]'],
        ['[H]','[Q]','[M]','[N]','[S]','[F]','[R]','[J]'],
        ['[R]','[N]','[F]','[H]','[W]'],
        ['[J]','[Z]','[T]','[Q]','[P]','[R]','[B]']]
        



# part 1
for l in moves.split('\n'):
    amt=int(l.split("from")[0].split('move')[-1].strip())
    start=int(l.split("from")[1].split('to')[0])-1
    end=int(l.split("from")[1].split('to')[1])-1
    
    for i in range(amt):
        stacks[end].append(stacks[start][-1])
        del stacks[start][-1]
        
ans=[]
for x in stacks:
    ans.append(x[-1])
    
print(ans)

stacks=[['[Q]','[S]','[W]','[C]','[Z]','[V]','[F]','[T]'],
        ['[Q]','[R]','[B]'],
        ['[B]','[Z]','[T]','[Q]','[P]','[M]','[S]'],
        ['[D]','[V]','[F]','[R]','[Q]','[H]'],
        ['[J]','[G]','[L]','[D]','[B]','[S]','[T]','[P]'],
        ['[W]','[R]','[T]','[Z]'],
        ['[H]','[Q]','[M]','[N]','[S]','[F]','[R]','[J]'],
        ['[R]','[N]','[F]','[H]','[W]'],
        ['[J]','[Z]','[T]','[Q]','[P]','[R]','[B]']]



# part 2
for l in moves.split('\n'):
    amt=int(l.split("from")[0].split('move')[-1].strip())
    start=int(l.split("from")[1].split('to')[0])-1
    end=int(l.split("from")[1].split('to')[1])-1
    
    tmp=[]
    for i in range(amt):
        tmp.append(stacks[start][-1])
        del stacks[start][-1]
    tmp.reverse()
    
    stacks[end]=stacks[end]+tmp
    
ans=[]
for x in stacks:
    ans.append(x[-1])
    
print(ans)


    
    




