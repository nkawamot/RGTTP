"""
  Lesson 4: ex1.py
"""

# 1. Create 'fruits' dictionary and add following key: values
# apple: 10
# orange: 2

# INSERT YOUR CODE HERE
fruits: dict[str, int] = {"apple": 10, "orange": 2}
print(fruits)


# 2. Add banana to the dictionary and set it's value to 3

# INSERT YOUR CODE HERE
fruits["banana"] = 3
print(fruits)


# 3. Add mandarin using dictionary method .update()

# INSERT YOUR CODE HERE
fruits.update({"mandarin": 1})
print(fruits)


# 4. Remove the mandarin from the dictionary

# INSERT YOUR CODE HERE
del fruits["mandarin"]
print(fruits)


# 5. Add 10 more apples and remove 2 bananas

# INSERT YOUR CODE HERE
fruits["apple"] += 10
fruits["banana"] -= 2
print(fruits)


# 6. Remove 'apple' from the dictionary using .pop()
#    and save it's value into a variable 'apples'

# INSERT YOUR CODE HERE
try:
    apples: int = fruits.pop("apple")
except KeyError as e:
    print(e)

print(apples)
print(fruits)


# 7. Remove 'mandarin' from the dictionary using .pop()
#    and save it's value into a variable 'mandarin'
#    if 'mandarin' doesn't exist set the variable to 0

# INSERT YOUR CODE HERE
try:
    mandarin: int = fruits.pop("mandarin")
except KeyError as e:
    mandarin: int = 0
    print(e)

print(mandarin)
print(fruits)


# 8. Remove last item from the dictionary using .popitem()
#    and save it's value into variable 'last'

# INSERT YOUR CODE HERE
try:
    last: int = fruits.popitem()
except KeyError as e:
    print(e)

print(last)
print(fruits)


# 9. Check if the 'banana' is in the fruits dictionary.

# INSERT YOUR CODE HERE
print("banana" in fruits)
