i=1
while i<=10:
    n=int(input("enter the number"))
    if i==1:
        max=min=n
    if n>max:
        max=n
    if n<min:
        min=n
    i=i+1
print("max",max)
print("min",min)


