# Write a Python program to guess a number between 1 to 9

n=int(input("enter the number"))
i=1
while i<=n:
    if n>=1 and n<=9:
        print(i)
    else:
        print("try again")
    i=i+1



