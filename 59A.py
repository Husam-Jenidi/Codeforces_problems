# importing Counter module
from collections import Counter

input_list = input("")


# creating a list with the keys
upp = sum(1 for c in input_list if c.isupper())
#print(upp)
low = sum(1 for c in input_list if c.islower())
#print(low)
#  if ord(input_list[el]) in range(65, 90): upp += 1, print(upp)
# elif ord(input_list[el]) in range(97, 122): low = low + 1, print(low)

if upp > low : print(input_list.upper())
else: print(input_list.lower())
