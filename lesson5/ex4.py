"""
  Lesson 5: ex4.py
"""

# 1. Write a function get_index() that returns the index of
#    a character in a string

# INSERT YOUR CODE HERE
def get_index(word: str, char: str) -> int:
    for index, letter in enumerate(word):
        if (letter == char):
            return index

print(get_index("redhat", "e"))
print("redhat".index("e"))


# 2. Write a function shout() that returns each word
#  capitalized with "!" and on it's own line.

# INSERT YOUR CODE HERE
def shout(sentence: str) -> None:
    for word in sentence.split(" "):
        print(f"{word.upper()}!")

shout("How are you doing?")


# 3. Write a function extract_longer() that extracts
#    words longer or equal to n-characters and return a list,
#    otherwise return False

# INSERT YOUR CODE HERE
def extract_longer(num: int, sentence: str) -> list | bool:
    result: list[str] = []
    for word in sentence.split(" "):
        if (len(word) >= num):
            result.append(word)
    return result if result else False

print(extract_longer(2, "How is it going?"))
print(extract_longer(3, "How is it going?"))
print(extract_longer(10, "How is it going?"))
