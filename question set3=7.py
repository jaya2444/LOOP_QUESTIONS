# Now, we will make a game using loops. We will call this game a guessing game.

# 1

# In this game we take any number, let us suppose this number is number 5.

# 2

# After this we take any number as an input from the user between 1 to 10. The user tries to guess this number.

# 3

# Suppose the user gives 3as an input. We will then check if 3 is equal to 5 or not?

# 4

# 3 is not equal to 5 so we will ask the user for another input.

# 5

# Now, we will check if that number is equal to 5 or not.

# 6

# User will get 5 chances to guess.

# If he guessed right within the 5 chances he wins and if he guesses wrong then loses the game.
# Hint :

# Study about break statement in python.




# n=5
# c=1
# while c<=5:
#     guess=int(input("enter number"))
#     if guess<=10 or guess<=1:
#         if guess==n:
#             print("u win")
#             break;
#     print("loss")
#     c=c+1


n=5
c=1
while c<=5:
    guess=int(input("enter the number"))
    if 10>guess>1:
        if guess==n:
            print("you win")
            break;
    print("sorry u loose")
    c=c+1