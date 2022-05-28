# Write a program to check whether a number is prime or not.

a=int(input("enter the number"))
while a>0:
    if a%2!=0 and a%3!=0 and a%5!=0 and a%7!=0:
            print(a,"prime number")
            break
    elif a==2 or a==3 or a==5 or a==7:
        print(a,"prime number")
        break
    else:
        print(a,"not prime")
        break
    