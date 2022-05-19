# Exercise 1: Create a list, tuple, float, integer, decimal, and dictionary.

from cmath import sqrt
from decimal import Decimal

list = ['vacation', 'car', 'hotel', 'budget']

tuple = ('CSCI 545', 'Spring', '2022')

float = 45.95

interger = 112

pi = Decimal(3.14)

dictionary = {
    "Red" : "Tomato",
    "Yellow" : "Banana",
    "Green" : "Grapes",
}

# Exercise 2: Round your float up.
print(round(float))

# Exercise 3: Get the square root of your float.
print(sqrt(float))

# Exercise 4: Select the first element from your dictionary.
# print(list(dictionary.items())[0])

# Exercise 5: Select the second element from your tuple.
print(tuple[1])

# Exercise 6: Add an element to the end of your list.
list.extend(['dates'])
print(list)

# Exercise 7: Replace the first element in your list.
list[0]= 'baecation'
print(list)

# Exercise 8: Sort your list alphabetically.
list.sort()
print(list)

# Exercise 9: Use reassignment to add an element to your tuple.
tuple += ('USC',)
print(tuple)