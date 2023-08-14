"""
  Lesson 3: ex4.py
"""

# 1. Create your own Shopping List type.
#
# a. Initialize the ShoppingList class with shopping_list
#    shopping_list = ['apples', 'milk', 'bread', 'carrot', 'pasta']
#
# b. Add in_list method, that checks if the item is in list or not,
#    use the format() or f-strings to return the string based on truth:
#    - 'apples' is in the shopping list.
#    - 'apples' not in the shopping list.
#
# c. Add special function when printing the list to output:
#    * Replace the list with {} and print using format().
#    My shopping list: ['apples', 'milk', 'bread', 'carrot', 'pasta']
#
# d. Add special function for comparison of two objects to output:
#    * Based on the truth.
#    - True
#    - False

# INSERT CODE HERE
class ShoppingList:
    def __init__(self, 
                 original_list=['apples', 'milk', 'bread', 'carrot', 'pasta']):
            self.shopping_list: list[str] = original_list


    def in_list(self, item) -> str:
        if item in self.shopping_list:
            return "'{}' is in the shopping list".format(item)
        else:
            return "'{}' is not in the shopping list".format(item)


    def __str__(self) -> str:
        return "My shopping list: {}".format(self.shopping_list)


    def __eq__(self, other) -> bool:
        if other is None or type(self) != type(other):
            return False
        return self.shopping_list == other.shopping_list


# Test for a
my_shopping_list = ShoppingList()

# Test for b
print(my_shopping_list.in_list("apples"))
print(my_shopping_list.in_list("coffee"))

# Test for c
print(my_shopping_list.__str__())

# Test for d
second_shopping_list = ShoppingList()
print(my_shopping_list.__eq__(second_shopping_list))
