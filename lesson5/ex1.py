"""
  Lesson 5: ex1.py
"""

# 1. Create even() function that return "I am even!" if number is even
#    or "I am odd!" if the number is odd.

# INSERT YOUR CODE HERE
def even(num: int) -> str:
    if (num % 2 == 0):
        return "I am even!"
    else:
        return "I am odd!"

print(even(2))
print(even(3))
#print(even("2"))


# 2. Create safe_even() function, that will output "I am not number!" if
#    the input is not an number otherwise will work same as even()

# INSERT YOUR CODE HERE
def safe_even(num: int) -> str:
    if not isinstance(num, int):
        return "I am not a number!"
    elif (num % 2 == 0):
        return "I am even!"
    else:
        return "I am odd!"

print(safe_even(2))
print(safe_even(3))
print(safe_even("2"))


# 3. Create a function fizz_buzz(),
#    replacing any number divisible by three with the word "fizz",
#    and any number divisible by five with the word "buzz",
#    and any number divisible by both 3 and 5 with the word "fizzbuzz",
#    and number if number is not divisible by any.

# INSERT YOUR CODE HERE
def fizz_buzz(num: int) -> str:
    if not isinstance(num, int):
        return "Not a number!"
    elif (num % 3 == 0) and (num % 5 == 0):
        return "fizzbuzz"
    elif (num % 3 == 0):
        return "fizz"
    elif (num % 5 == 0):
        return "buzz"
    else:
        return str(num)

print(fizz_buzz(3))
print(fizz_buzz(5))
print(fizz_buzz(15))
print(fizz_buzz(1))
print(fizz_buzz("3"))


# 4. Execute fizz_buzz() function from 1 to the 100

# INSERT YOUR CODE HERE
for i in rnage(1, 101):
    print(fizz_buzz(i))
