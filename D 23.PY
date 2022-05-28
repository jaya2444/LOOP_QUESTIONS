# Write a program to accept 10 numbers from the user and display the largest & smallest number.



i=1
while i<=10:
    n=int(input("enter the number"))
    if i==1:
        largest=smallest=n
    if n>largest:
        largest=n
    if n<smallest:
        smallest=n
    i+=1
print("largest is",largest)
print("smallest is",smallest)