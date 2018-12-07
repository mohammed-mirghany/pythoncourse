def seeprimes(num):
    newlist=[]
    
    for i in range(2,num+1):
        
        for k in range(2,i):
            if i %k!=0:
                newlist.append(i)
        	continue
            
        
    print(newlist)

seeprimes(100)