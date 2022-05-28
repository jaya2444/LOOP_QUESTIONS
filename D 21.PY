# Write a python program to sum the sequence:
# 1 + 1/1! + 1/2! + 1/3! + …….. + 1/n!


n=int(input("enter the number"))
i=0
sum=1
while n>0:
    i=1/n
    sum=sum+i
    n=n-1          
print(sum)


 