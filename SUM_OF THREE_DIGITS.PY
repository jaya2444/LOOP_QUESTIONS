n=int(input("enter the number"))
i=0
while n>i:
    x=n//100%10
    y=n//10%10
    z=n%10
    m=x+y+z
    i=i+1
print(m) 