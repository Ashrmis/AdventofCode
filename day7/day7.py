commands=[ line.strip() for line in open('test.txt')]

storage=[]
ls_ct=0

for x in range(len(commands)):
    if commands[x]== "$ ls":
        print(x)
        go=True
        i=x
        dirc=[]
        tmp=[]
        
        while go and i!=len(commands):
            
            try:
                nextCmd=commands[i+1]
            except IndexError:
                go=False
                for a in dirc:
                    try:
                        size=int(a.split(' ')[0])
                        tmp.append(size)    
                    except ValueError:
                        pass
                storage.append(sum(tmp))
                print(" ",(tmp))
                break
            
            if 'ls' in nextCmd:
                go=False
                for a in dirc:
                    try:
                        size=int(a.split(' ')[0])
                        tmp.append(size)    
                    except ValueError:
                        pass
                storage.append(sum(tmp))
                print(" ",(tmp))
                break
            
            dirc.append(commands[i+1])
            i=i+1

            
            

        
            

            

                
        
        
    

    
    

        