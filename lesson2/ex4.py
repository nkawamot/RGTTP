"""
  Lesson 2: ex4.py
"""

# 1. Print the formatted keys and values of the dictionary.
#    versions: dict[str, int] = {'Stein': 15, 'Train': 16, 'Wallaby': 17}

# INSERT YOUR CODE HERE
versions: dict[str, int] = {"Stein": 15, "Train": 16, "Wallaby": 17}

for codename, version in versions.items():
    print("codename: {0:>7s}, version: {1:>02d}".format(codename, version))


# 2. Print {} around the version numbers.

# INSERT YOUR CODE HERE
for codename, version in versions.items(): 
    print("codename: {0:>7s}, version: {{{1:>02d}}}".format(codename, version))


# 3. Print numbers in decimal, byte and hexadecimal form.

# INSERT YOUR CODE HERE
for codename, version in versions.items():
    print("codename: {0:>7s}, "
          "version(in decimal): {1:>02d}, "
          "version(in byte): {1:>06b}, " 
          "version(in hexadecimal): {1:>02x}".format(codename, version))
