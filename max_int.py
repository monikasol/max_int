# Design an algorithm that finds the maximum positive integer input by a user.  
# The user repeatedly inputs numbers until a negative value is entered.

num = int(input('Input a number: '))

max_num = 0

while num >= 0:
    if num >= max_num:
        max_num = num
    num = int(input('Input a number: '))

print("the maximum positive number is: ", max_num)

 