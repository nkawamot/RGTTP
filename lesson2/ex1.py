"""
  Lesson 2: ex1.py
"""

# 1. Create a format string to display the name and age of a person.

# INSERT YOUR CODE HERE
name: str = "Nozomi"
age: int = 27
print("My name is {0:s}. I'm {1:d} years old.".format(name, age))


# 2. Print version with it's corresponding upstream codename,
#    and use padding aligned format to left, centre and right.

# INSERT YOUR CODE HERE
osp_versions: dict[int, str] = {13:"Queens", 16:"Train", 17:"Wallaby"}

for version, codename in osp_versions.items():
    print("RHOSP {0:d} is based on {1:<20s}!".format(version, codename))
    print("RHOSP {0:d} is based on {1:^20s}!".format(version, codename))
    print("RHOSP {0:d} is based on {1:>20s}!".format(version, codename))


# 3. Show different representations of an integer.

# INSERT YOUR CODE HERE
x: int = 10

print("{:d} is {:^10b} in base 2".format(x,x))
print("{:d} is {:^10o} in base 8".format(x,x))
print("{:d} is {:^10d} in base 10".format(x,x))
print("{:d} is {:^10x} in base 16".format(x,x))


# 4. Format a floating-point number with fixed precision.

# INSERT YOUR CODE HERE
print("{:d} is {:^.2f}".format(x,x))
