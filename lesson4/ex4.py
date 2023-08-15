"""
  Lesson 4: ex4.py
"""

# 1. Create a data variable which contains a list of objects
#    with following key and values:
#    {"category": "fruit", "name": "apple"}
#    {"category": "fruit", "name": "banana"}
#    {"category": "fruit", "name": "orange"}
#    {"category": "vegetable", "name": "carrot"}
#
#    Write a for loop to print out the fruits and vegetables.
data: list[dict[str, str]] = [
    {"category": "fruit", "name": "apple"},
    {"category": "fruit", "name": "banana"},
    {"category": "fruit", "name": "orange"},
    {"category": "vegetable", "name": "carrot"}
]

categorized_dict: dict[str, list[str]] = {}

for obj in data:
    category = obj["category"]
    if category in categorized_dict:
        categorized_dict[category].append(obj["name"])
    else:
        categorized_dict[category] = [obj["name"]]

print(categorized_dict)
