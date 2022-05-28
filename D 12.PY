# Write a program to find the product of the digits of a number accepted from the user.

n=int(input("enter the number"))
product=1
while n!=0:
    product=product*(n%10)
    n=n//10
print(product)
