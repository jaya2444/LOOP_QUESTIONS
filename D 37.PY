
# Write a program to print the factorial of a number.


n=int(input("enter the number"))
fact=1
while n>0:
    fact=fact*n
    n=n-1
print(fact)