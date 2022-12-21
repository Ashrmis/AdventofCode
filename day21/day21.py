# part 1
lines=[line.strip() for line in open("day21in.txt")]
m={}
for x in lines:
    name,form=x.split(": ")
    
    if form.isdigit():
        m[name]=int(form)
    else:
        left,op,right=form.split()
        
        if left in m and right in m:
            m[name]= eval(f"{m[left]} {op} {m[right]}")
        else:
            lines.append(x)
            
# part 2 ???