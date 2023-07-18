"""
  Lesson 1: ex3.py
"""

# 1. Print out your favourite food 42 times using * operator.

# INSERT YOUR CODE HERE
print("ramen"*42)

# 2. Insert space between each output and print it out again.

# INSERT YOUR CODE HERE
print(" ".join(["ramen"]*42))

# 3. Save your favourite food into a variable and print it out 42 times

# INSERT YOUR CODE HERE
my_favorite_food: str = "ramen"
print(my_favorite_food*42)

# 4. My favourite food is "sushi", save it into a variable and using
#    fast swapping operation change it with your variable.
#    Now your favourite food should be "sushi" and mine will be yours.#

# INSERT YOUR CODE HERE
your_favorite_food: str = "sushi"
my_favorite_food, your_favorite_food = your_favorite_food, my_favorite_food
