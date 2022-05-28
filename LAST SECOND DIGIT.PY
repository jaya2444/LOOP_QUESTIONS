n=int(input("enter the number"))
a=n
while a>=n:
    a=a//10%10
    print(a)
    
# n=int(input("enter the number"))
# a=n//10
# b=a%10
# i=0
# while i<=n:
#     i=i+1
# if b==2:
#     print(b,"true")
# else:
#     print(b,"false")

n=int(input("enter the number"))
a=n//10
b=a%10
if n>0:
 print(b,"it is second last digit")
else:
    print("nothing")