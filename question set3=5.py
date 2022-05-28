# Take input of weights of 11 people and then print their average and then check whether the average weight is a multiple of 5 or not? This means that when you will divide the average weight by 5, the remainder should be 0.
# Note :-

# Here you have to use input function. You can also use raw input to take the weights as inputs, inside the loop.


i=1
sum=0
while i<=11:
    weight=float(input("enter the weight"))
    sum=sum+weight
    i=i+1
print(sum)
avg=sum/11
if avg%5==0:
    print("it is divisible by 5")
else:
    print("it is not divisible by 5")