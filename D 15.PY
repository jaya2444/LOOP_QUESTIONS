# Write a program to print the Fibonacci series till n terms (Accept n from user)



x=0
y=1
i=0
n=int(input("enter the number"))
while i<=n:
    print(i)
    x=y
    y=i
    i=x+y

