# Write a program to print all the factors of a number using a while loop .

# n=int(input("enter the number"))
# i=0
# while i<=n:
#     i=i+1
#     if n%i==0:
#         print(i)

n=int(input("enter the number"))
i=1
while i<=n:
    if n%i==0:
        print(i)
    i=i+1
