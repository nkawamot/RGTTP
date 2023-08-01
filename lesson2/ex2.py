"""
  Lesson 2: ex2.py
"""

# 1. Use string formatting with empty curly brackets {}
#    to take the argument passed into format and print a
#    sentence of your choice.

# INSERT YOUR CODE HERE
name: str = "Nozomi"
print("I'm {}.".format(name))


# 2. Use string formatting with positional arguments and
#    print the sentence: "Don't Panic!"

# INSERT YOUR CODE HERE
x: str = "Don't"
y: str = "Panic!"
print("{0} {1}".format(x, y))


# 3. Use string formatting with named arguments and
#    print the sentence: "[name] is really [what]!" and
#    fill in the brackets with your name and "great".

# INSERT YOUR CODE HERE
print("{name:s} is really {what:s}!".format(name="Nozomi", what="great"))
