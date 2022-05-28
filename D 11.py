# Write a program to find the sum of the digits of a number accepted from the user.


n=int(input("enter the number"))
sum=0
while n!=0:
    sum=sum+(n%10)
    n=n//10
print(sum)
