#Exercise 1: Create a string, number, list, and boolean, each stored in their own variable.

# string
my_name = "Michael"

# number
my_age = 32

# list
list_of_siblings = ['Billy', 'Sean', 'Kieth', 'Monica', 'Brandy']

# boolean
phone = True

#Exercise 2: Use an index to grab the first 3 letters in your string, store that in a variable. 

print(my_name[0:3])

partial_name = my_name[0:3]

print(partial_name)

#Exercise 3: Use an index to grab the first element from your list.

print(list_of_siblings[0])

#Exercise 4: Create a new number variable that adds 10 to your original number.

plus_ten = 10 + my_age

print(plus_ten)

#Exercise 5: Use an index to get the last element in your list.

print(list_of_siblings[-1])

#Exercise 6: Use split to transform the following string into a list.
	
names = 'harry,alex,susie,jared,gail,conner'

list_of_names = names.split(',')

print(list_of_names)

#Exercise 7: Get the first word from your string using indexes. Use the upper function to transform the letters into uppercase. Create a new string that takes the uppercase word and the rest of the original string.

print(list_of_names[0].upper() + str(list_of_names[1:]))

#Exercise 8: Use string interpolation to print out a sentence that contains your number variable.

print(str('I turned ') + str(my_age) + str(' last year. This year I will turn 33'))

#Exercise 9: Print “hello world”.

print('Hello world')