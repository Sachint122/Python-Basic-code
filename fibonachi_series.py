def sun(n):
    f1=1
    f0=0
    if(n==1 or n==0):
        return 1
    else :
        print((sun(n-1)+sun(n-2)))
        return (sun(n-1)+sun(n-2))
        

sun(10)