def vivod(pos):       
    for i in range(len(pos)-1):        
        n=0
        for j in range(i+1, len(pos)):            
            if pos[i]==pos[j]:
                pos[j]='p'
                n+=1
        if n!=0:
            pos[i]='p'
    rez=[]
    for i in range(len(pos)):
        if pos[i]!='p':
            rez.append(pos[i])
    print(rez) 

pos = [1, 2, 2, 3, 4, 4, 5]
vivod(pos)