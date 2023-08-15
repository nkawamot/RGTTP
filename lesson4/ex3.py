"""
  Lesson 4: ex3.py
"""

# 1. Create dictionary using comprehension
# {key, value = i, i**2}

# INSERT YOUR CODE HERE
first_dict: dict[int, int] = {i: i**2 for i in range(10)}
print(first_dict)


# 2. Create another comprehension and add +1 to each key's value.
# {key, value = i, i+1}

# INSERT YOUR CODE HERE
second_dict: dict[int, int] = {i: i+1 for i in range(10)}
print(second_dict)


# 3. Create 'fruits' defaultdict():
# apple: 10
# orange: 2
# banana: 3
# and for any other key set it's default value to 0

# INSERT YOUR CODE HERE
from collections import defaultdict
from typing import Any

fruits: defaultdict[Any, Any] = defaultdict(int)
fruits.update({"apple": 10, "orange": 2, "banana": 3})
print(fruits)
print(fruits["mandarin"])


# 4. Sort the 'fruits' dictionary using sorted() method
# by keys and values, dictionary does not have .sort()

# INSERT YOUR CODE HERE
print(sorted(fruits.keys()))
print(sorted(fruits.values()))


# 5. Return 'sorted_fruits' dictionary using sorted() method,
# sort by values.

# INSERT YOUR CODE HERE
def sort_by_value(item) -> int:
    return item[1]

sorted_fruits: list[tuple[str, int]] = sorted(fruits.items(), key=sort_by_value)
print(dict(sorted_fruits))


# 6. Reverse the 'sorted_fruits' dictionary and print the dictionary.

# INSERT YOUR CODE HERE
reversed_fruits: list[tuple[str, int]] = reversed(sorted_fruits)
print(dict(reversed_fruits))
