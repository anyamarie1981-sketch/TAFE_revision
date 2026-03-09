# 06 - Lists and Dictionaries - Q1-Q9

# File: C:\Users\dandy\OneDrive\TAFE - Onedrive\
# ICTPRG302 - Apply introductory programming techniques - ICT40120 (Programming) - Sem 1 2026\
# Revision\WK 06\06_lists_and_dictionaries_fruits.py
# Author: Anya Polmear
# Copyright 2026: Anya Polmear 2026

print("1. Create a List of Fruits, print list")
fruits = ["grapes", "kiwi", "pawpaw"]
print(fruits)

print("\n2. Access an element by Index, print 2nd item")
print(fruits[1])

print("\n3. Ad an items to a list and print")
fruits.append("strawberry")
print(fruits)

print("\n4. Relace an item in a list and print (Change first item)")
fruits[0] = "cherry"
print(fruits)

print("\n5. Check if an item exists in a list, check for apple")
if "apple" in fruits:
    print("Apple crumble for dessert")
else:
    print("There's no apples for apple crumble")
    
print("\n6. Print all fruits using a loop")
for each in fruits:
    print(each)
    
print("\n7. Count items in a list using loop, not using len()")
list_len = 0
for each in fruits:
    list_len += 1
print(list_len)

print("\n8. Find the longest fruit name using a loop")
print("9. Create a list of fruit name lengths")
fruit_len = []
for each in fruits:
    each_len = len(each)
    fruit_len.append(each_len)
print(f"List of fruit name lengths: {fruit_len}")
print(f"Largest length in fruit_len: {max(fruit_len)}")
len_index = fruit_len.index(max(fruit_len))
print(f"Index number in the fruit_len list: {len_index}")
print(f"Fruit with longest name: {fruits[len_index]}")
