# 1
# 2 3
# 4 5 6
# 7 8 9 10

a=1
i=1
while i<=4:
    j=1
    while j<=i:
        print(a,end=" ")
        j=j+1
        a=a+1
    print()
    i=i+1