import math

loss = -20.12
product_cost = 89.12

print(abs(loss))
print(math.floor(product_cost))
print(math.ceil(product_cost))
print(abs(math.floor(loss))) # floor is the lower value so this goes more negative to -21 first
print(round(product_cost))
print(math.sqrt(product_cost))
print(math.pow(5, 2))
print(5 ** 2) #gives interger value vs. pow giving floating point (more accurate)

heading = "Python: An Introduction: an exam"

heading, subheading, sub_sub = heading.split(': ')

print(heading)
print(subheading)
print(sub_sub)