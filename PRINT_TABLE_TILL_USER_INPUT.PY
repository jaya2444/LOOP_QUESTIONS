n1=int(input("enter the number"))
n2=int(input("enter the number"))
i=n1
while n2:
    j=1
    while j<=n2:
        print(i,"*",j,"=",i*j)
        j=j+1
    print()
    i=i+1
    break


n1=int(input("enter the number"))
n2=int(input("enter the last number"))
i=1
while i<=n2:
    print(n1,"*",i,"=",n1*i)
    i=i+1



number_1=int(input("enter the number"))
number_2=int(input("enter the second number"))
while number_1<=number_2:
    print(number_1,"*",number_2,"=",number_1*number_2)
    number_1=number_1+1
