"""
  Lesson 2: ex3.py
"""

# 1. Create a list containing three elements representing the
#    name, age, and occupation of a person.
#    Then, print the sentence using the elements with .format()

# INSERT YOUR CODE HERE
personal_information: list[str] = ["Nozomi", "27", "TSE"]
print("{data[0]:s} is {data[1]:s} years old. "
      "And he is working as a {data[2]:s}.".format(data=personal_information))


# 2. The dictionary should contain keys such as
#    'title', 'author', and 'publication_year'.
#    Use the .format() method with multiple positional arguments.
#    Example:
#    "The guidebook [title] by [author] was published in [publication_year]."

# INSERT YOUR CODE HERE
book_information: dict[str, str] = {"title":"Harry Potter", "author":"J.K. Rowling", "publication_year":"1997"}
print("The book {data[title]:s} by {data[author]:s} was "
      "published in {data[publication_year]:s}.".format(data=book_information))


# 3. The dictionary should hold details about a spaceship, such as
#    'name', 'type', and 'purpose'.
#    Use the .format() method with named arguments.
#    Example:
#    "The spaceship is called the [name]. It is a [type] used for [purpose]."

# INSERT YOUR CODE HERE
spaceship_information: dict[str, str] = {"name":"Cassini", "type":"Orbiter", \
                                        "purpose":"Saturn Orbiter"}
print("The spaceship is called the {data[name]:s}. "
      "It is a {data[type]:s} used for {data[purpose]:s}.".format(data=spaceship_information))
