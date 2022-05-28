string=input("enter any string")
i = len(string)-1
sum = ''
while i>=0:
    sum=sum+string[i]
    i=i-1
if string == sum :
    print("palindrome")
else:
     print("not palindrome")