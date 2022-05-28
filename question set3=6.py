# Write a code to print this pattern.

# 1, -2, 3, -4, 5, -6 ..99, -100




i=1
while i<=200:
    if i%2==0:
        print(-i,end=" ")
    else:
        print(i,end=" ")
    i=i+1
    if i==101:
        break;...
