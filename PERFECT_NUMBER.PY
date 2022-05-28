# 28=1,2,4,7,14,28
#    1+2+4+7+14=28 means it is perfect number
# 6=1,2,3,6
#   1+2+3=6 mean it is perfect number



num=int(input("enter the number"))
sum=0
i=1
while i<num:
    if num%i==0:
        sum=sum+i
    i=i+1
if num==sum:
    print(num,"is a perfect number")
else:
    print(num,"is not perfect number")