# Write a program to check whether a number is Armstrong or not. (Armstrong number is a number that is
# equal to the sum of cubes of its digits, for example : 153 = 1^3 + 5^3 + 3^3.)


# FOR ONLY THREE DIGITS......

# i=0
# num=int(input("enter the number"))
# while i<=num:
#     a=(num//100%10)**3
#     b=(num//10%10)**3
#     c=(num%10)**3
#     sum=a+b+c
#     i=i+1
# if num==sum:
#     print("it is a armstrong")
# else:
#     print("it is not a armstrong")


# FOR ALL DIGITS......

# n=int(input("enter the number"))
# a=n
# sum=0
# order=len(str(n))
# while n>0:
#     digit=n%10
#     sum=sum+digit**order
#     n=n//10
# if sum==a:
#     print("armstrong")
# else:
#     print("not armstrong")
