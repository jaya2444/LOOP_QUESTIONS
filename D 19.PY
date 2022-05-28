# Write a program to add first n terms of the following series using a while loop :
# 1/1! + 1/2! + 1/3! + …….. + 1/n!


n=int(input("enter the number"))
i=0
while i<=n:
    print(1,"/",i,"!","+",end="")
    i=i+1

