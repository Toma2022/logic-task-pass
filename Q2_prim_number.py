k=int(input("input range 1"))
b=int(input("input range 2"))

for j in range(k,b+1):
    
    if k > 1:
        for i in range(2, int(k/2)+1):
             if (k % i) == 0:
                
                break
        else:
            print(k,)
    
  
    k=k+1