from email.base64mime import header_length
from functools import reduce
from logging import getLogRecordFactory



def manual_exponent(num, exp):
    counter = exp - 1
    total = num

    while counter > 0:
        total *= num #same thing as total = totatl * num
        counter -= 1 #same as counter = counter -1

    return total

print(manual_exponent(2, 3))
print(manual_exponent(10, 2))

def manual_exponent2(num, exp):
    computed_list = [num] * exp
    return (reduce(lambda total, element : total * element, computed_list))

print(manual_exponent2(2, 3))
print(manual_exponent2(10, 2))