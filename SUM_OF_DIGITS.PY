num=int(input("enter the number"))
sum=0
i=1
while i<=num:
    sum=sum+num%10
    num=num//10
i=i+1
print(sum)
