"""
  Lesson 5: ex2.py
"""

# 1. Write a while true loop to print "Forever" forever

# INSERT YOUR CODE HERE
while True:
    print("Forever")


# 2. Write a while loop to print numbers from 0 to 42

# INSERT YOUR CODE HERE
num: int = 0
while (num <= 42):
    print(num)
    num += 1


# 3. Write a while true loop to print numbers from 0 to 42

# INSERT YOUR CODE HERE
num: int = 0
while True:
    if (num > 42):
        break 
    print(num)
    num += 1


# 4. Write a while true loop to print numbers from 0 to 45, and instead
#    of 42, print "I am 42!" break at number 45.

# INSERT YOUR CODE HERE
num: int = -1
while True:
    num += 1
    if (num > 45):
        break
    elif (num == 42):
        print("I am 42!")
        continue
    print(num)


# 5. Write a while-else loop to count to 2, and after that print
#    "It's my turn now!" using else statement.

# INSERT YOUR CODE HERE
num: int = 0 
while num < 3:
    print(num)
    num += 1
else:
    print("It's my turn now!")
