# Write a program to find the sum of following series:
# S = 1 + 4 – 9 + 16 – 25 + 36 – … … n terms



n=int(input("enter the number"))
i=1
while i<=n:
    if i%2==0:
        print(i**2,end="")
    else:
        print((i**2)*(-1),'+',end="")
    i=i+1


# n=int(input("enter the number"))
# i=1
# while i<=n:
#     if i%2==0:
#         print(i**2,end="")
#     else:
#         print((i**2)*(-1),'+',end="")
#     i=i+1
