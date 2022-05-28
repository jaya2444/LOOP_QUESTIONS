#         1
#       2 1
#     3 2 1
#   4 3 2 1
# 5 4 3 2 1

i=5
while i>=1:
    b=1
    while b<=i-1:
        print(" ",end=" ")
        b=b+1
    j=6
    while j>i:
        print(j-i,end=" ")
        j=j-1
    print()
    i=i-1