# reverse number of digits

# n=int(input("enter the number"))
# rev=0
# while n>0:
#     rev=(rev*10)+n%10
#     n=n//10
# print("reverse number of digits",rev)


#sum of digits

# n=int(input("enter the number"))
# sum=0
# while n>0:
#     sum=sum+n%10
#     n=n//10
# print("sum of digits",sum)

#factorial number

# n=int(input("enter the number"))
# fact=1
# while n>0:
#     fact=fact*n
#     n=n-1
# print("factorial of number",fact)

#fibonacci series

# x=0
# y=1
# z=0
# n=int(input("enter the number"))
# while z<=n:
#     print(z)
#     x=y
#     y=z
#     z=x+y

# table print from n1 to n2

# n1=int(input("entre the number"))
# n2=int(input("enter the last number"))
# i=1
# while i<=n2:
#     print(n1,"*",i,"=",n1*i)
#     i=i+1

# factors  of number

# n=int(input("enter the number"))
# i=1
# while n>0:
#     if n%i==0:
#         print(i)
#     i=i+1

#palindrome number

# n=int(input("enter the number"))
# a=n
# rev=0
# while n>0:
#     rev=(rev*10)+n%10
#     n=n//10
# if a==rev:
#     print("it is palindrome number")
# else:
#     print("it is not palindrome number")

#palindrome string

# string=input("enter any string")
# i=len(string)-1
# sum=""
# while i>=0:
#     sum=sum+string[i]
#     i=i-1
# if string==sum:
#     print("it is palindrome string")
# else:
#     print("it is not palindrome string")

#perfect number

# num=int(input("enter the number"))
# sum=0
# i=1
# while i<num:
#     if num%i==0:
#         sum=sum+i
#     i=i+1
# if num==sum:
#     print(num,"is perfect number")
# else:
#     print(num," is not perfect number")

#harshad number

# n=int(input("enter the number"))
# a=n
# sum=0
# while n>0:
#     sum=sum+n%10
#     n=n//10
# if a%sum==0:
#     print(a,"is harshad number")
# else:
#     print(a,"is not harshad number")

# prime number

# n=int(input("enter the number"))
# count=0
# i=1
# while i<=n:
#     if n%i==0:
#         count=count+1
#     i=i+1
# if count==2:
#     print("it is prime number")
# else:
#     print("it is not prime number")


    

# armstrong number

# n=int(input("enter the number"))
#  a=n
# sum=0
# order=len(str(n))
# while n>0:
#     digit=n%10
#     sum=sum+digit**order
#     n=n//10
# if sum==a:
#     print("it is armstrong number")
# else:
#     print("it is not armstrong")

# 1 to 10 number print but start from 55

# i=55   
# while i<65:
#     n=i-54
#     print(n)
#     i=i+1

# 5 to 14 number print start from 76

# i=76
# while i<=85:
#     n=i-71
#     print(n)
#     i=i+1

# reverse number 17 to 1 but start from 35

# i=35
# while i>18:
#     n=i-18
#     print(n)
#     i=i-1

# reverse number 100 to 1 but start from 556

# i=556
# while i>456:
#     n=i-456
#     print(n)
#     i=i-1

# maximum number

# n=int(input("enter the number"))
# i=0
# max=0
# while i<n:
#     b=int(input("enter the number"))
#     if i==0:
#         max=b
#     elif b>max:
#         max=b
#     i=i+1
# print(max)

# happy and sad number

# n=int(input("enter the number"))
# a=n
# i=0
# while i==0:
#     sum=0
#     while a!=0:
#         su    while n>0:
            # if order!=1:
#             digit=n%10
#             sum=sum+(digit**order)
#             n=n//10m=sum+pow(a%10,2)
# #         a=a//10
#     if sum>9:
#         a=sum
#     else:
#         i=1
# if sum==1:
#     print(n," is happy number")
# else:
#     print(n," is sad number")

# product of the digits

# n=int(input("enter the number"))
# product=1
# while n>0:
#     product=product*n%10
#     n=n//10
# print("product of digits",product)

# convert binary to decimal

# bin=int(input("enter the binary number"))
# i=0
# sum=0
# while bin>0:
#     sum=sum+(bin%10)*(2**i)
#     i=i+1
#     bin=bin//10
# print(sum)

# last digit

# n=int(input("enter the number"))
# a=n%10
# i=0
# while i<=n:
#     i=i+1
# print(a)
# 
# n=int(input("enter the number"))
# a=n
# i=0
# while a>=n:
#     a=a%10
#     print(a)
#     i=i+1


#from last second digit

# n=int(input("enter the number"))
# a=n//10%10
# i=0
# while i<=n:
#     i=i+1
# print(a)

# n=int(input("enter the number"))
# a=n
# i=0
# while a>=n:
#     a=a//10%10
#     print(a)
#     i=i+1

# n=int(input("enter the number"))
# sum=0
# i=1
# while i<n:
#     if n%i==0:
#         sum=sum+i
#     i=i+1
# if n==sum:
#     print("perfect")
# else:
#     print("not perfect")


# n=int(input("enter the number"))
# i=1
# while i<=n:
#     if n%i==0:
#         print(i)
#     i=i+1


# n=int(input("enter the number"))
# a=n%10
# while n>0:
#     if a%5==0:
#         print("true")
#     else:
#         print("false")
#     break