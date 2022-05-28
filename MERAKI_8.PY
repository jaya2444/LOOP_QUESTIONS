
# Question 2

# Make a program that should do the following thing from 1 to 100.

# 1

# Numbers that are divisible by 3, you have to print "Nav".

# 2

# Numbers that are divisible by 7 so that "Gurukul" is printed.

# 3

# Numbers that are divisible by both 3 and 7, print "NavGurukul" there.

n=1
while n<=100:
    if n%3 and n%7==0:
        print("navgurukul")
    elif n%3==0:
        print("nav")
    elif n%7==0:
        print("gurukul")
    else:
        print(n)
    n=n+1
    