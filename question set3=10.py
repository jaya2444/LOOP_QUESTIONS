# Question 10

# Make an algorithm that prints the first 100 numbers of the fibonacci series.

# Fibonacci series is shown here,
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

# In this series first_number is 0 andsecond_number is 1. After this, the next number will be the sum of the last two numbers.
# Like, third_number = first_number + second_number
# 1 = 0 + 1
# fourth_number = second_number + third_number
# 2 = 1 + 1
# Hint :

# Now, think about how you can access the current counter and previous counter value.




x=0
y=1
z=0
while z<=100:
    print(z)
    x=y
    y=z
    z=x+y