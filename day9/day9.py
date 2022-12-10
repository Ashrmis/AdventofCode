moves = open("test.txt").read().strip().split("\n")

deltas={"R":[1,0],"L":[-1,0],"U":[0,1],"D":[0,-1]}

Hx,Hy,Tx,Ty=0,0,0,0 # starting locations

T_coordinates={}

def DiagMove(hx,hy,tx,ty):
    return (hx !=tx and hy!=ty)
        

for mv in moves:
    dirc=mv[0]
    steps=int(mv[2])
    
    dx,dy=deltas[dirc]
    
   
    for x in range(steps):
        Hx=Hx+dx
        Hy=Hy+dy
        
        if abs(Hx-Tx) >1 or abs(Hy-Ty) >1:
            
            if dirc=="R":
                if DiagMove(Hx,Hy,Tx,Ty):
                    Tx=Tx+1
                    Ty=Ty+(Hy-Ty)
                else:
                    Tx=Tx+1
               
            if dirc =="L":
                if DiagMove(Hx,Hy,Tx,Ty):
                    Tx=Tx-1
                    Ty=Ty+(Hy-Ty)
                else:
                    Tx=Tx-1
            if dirc == "U":
                if DiagMove(Hx,Hy,Tx,Ty):
                    Tx=Tx+(Hx-Tx)
                    Ty=Ty+1
                else:
                    Ty=Ty+1
            if dirc == "D":
                if DiagMove(Hx,Hy,Tx,Ty):
                    Tx=Tx+(Hx-Tx)
                    Ty=Ty-1
                else:
                    Ty=Ty-1
                
        if abs(Hx-Tx) <=1 and abs(Hy-Ty) <=1:
            print("touching",[Hx,Hy],[Tx,Ty])
            T_coordinates[(Tx,Ty)]=""
    print(mv)
    
    print('')
    
print(len(T_coordinates),'locations')
    
    