# Accept two numbers from the user and display sum of even numbers between them(including both)
        
n1=int(input("enter the number"))
n2=int(input("enter the second number"))
i=n1
sum=0
while i<=n2:
    if i%2==0:
        sum=sum+i
    i=i+1
print(sum)
