# Write a program to find the sum of the following series(accept values of x and n from user)
# 1 + x/1! + x2/2! + ……….xn/n!
# x + x2/2 + ……….xn/n


x=int(input("enter the number"))
n=int(input("enter the number"))
i=0
sum=1
fac=1
while n>0:
    fac=((1/n)*(x**i))
    sum=sum+fac
    n=n-1
    i=i+1
print(sum)
