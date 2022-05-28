# 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1

i=5
while i>=1:
    j=6
    while j>i:
        print(j-i,end="")
        j=j-1
    print()
    i=i-1