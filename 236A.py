# importing Counter module
from collections import Counter

input_list = input("")
# creating a list with the keys
items = Counter(input_list).keys()
if len(items) % 2 == 0: print("CHAT WITH HER!")
if len(items) % 2 != 0: print("IGNORE HIM!")