def d2b(n):
 
    if(n > 1):
        d2b(n//2)
 
     
    print(n%2+' ')