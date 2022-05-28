i=1
while i<1000:
    n=i
    a=n
    sum=0
    order=len(str(n))
    while n>0:
        digit=n%10
        sum=sum+digit**order
        n=n//10
    if sum==a:
        print(i,"is armstrong number")
    else:
        pass
    i+=1
