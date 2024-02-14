f={0:1,1:1,2:2}
def fat(n):
    global f
    if n<0:
        return -1
    #achar o maior resultado de fatorial que esteja mais proximo de n!
    ultimo_fat=n
    while f.get(ultimo_fat,0) == 0:
        ultimo_fat-=1
        
    #ultimo fat encontrado
    r = f.get(ultimo_fat)
    
    #começa calcular a partir do proximo valor ate o n
    for i in range(ultimo_fat+1,n+1):
        r*=i
        f[i]=r
   
    return r
    
def binomial(*,x,p,n):
  
    return fat(n)/(fat(x)*fat(n-x))*p**x*(1-p)**(n-x)
    

binomial2 = lambda x,p,n: (fat(n)/(fat(x)*fat(n-x)))*(p**x)*((1-p)**(n-x))

print(binomial(x=5,p=3,n=7))
print(binomial2(5,3,7))
