# Write a program to display all even numbers that fall between two numbers (exclusive both numbers)
# entered by the user.


n1=int(input("enter the number"))
n2=int(input("enter the number"))
i=n1
while i<=n2:
    if i%2==0:
        print(i)
    i=i+1

# a=int(input("enter the number"))
# b=int(input("enter the number"))
# while a<=b:
#     print(a)
#     a=a+2
                
        
