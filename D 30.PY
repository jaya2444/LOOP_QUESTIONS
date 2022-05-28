# Write a program to find the sum of following series
# 1 + 8 + 27 …………n terms



n=int(input("enter the number"))
sum=0
i=1
while i<=n:
    sum=sum+i**3
    i=i+1
print(sum)





