# Write a program to convert binary to decimal.

bin=int(input("enter the binary number"))
i=0
sum=0
while bin>0:
    sum=sum+(bin%10)*(2**i)
    i=i+1
    bin=bin//10
print(sum)


