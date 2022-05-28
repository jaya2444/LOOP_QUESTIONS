#  Write a program to print only odd numbers from the given list using a while loop . L = [23, 45, 32, 25, 46,
# 33, 71, 90]

a=[23,45,32,25,33,71,90]
i=0
while i<len(a):
    if a[i]%2==0:
        print(a[i])
    else:
        pass
    i=i+1