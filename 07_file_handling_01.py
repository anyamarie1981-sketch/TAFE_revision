# File Handling 01

# File: C:\Users\dandy\OneDrive\
#   TAFE - Onedrive\Tafe_revision\07_file_handling_01.py
# Author: Anya Polmear
# Copyright 2026: Anya Polmear 2026

"""
1. Reading
Try reading the contents of example.txt . Print each line, without trailing newlines.
2. Writing
Write "Hello, world!" to a file called my_file.txt . Visually inspect the contents.
3. Truncation?
Now write "Good evening" in the same my_file.txt . What do you notice has happened to
the file?
4. Appending
Write a program that asks for a user input, and appends it to my_file.txt .
5. But now, with loops
Make a loop of the above, so that the user can keep inputting text until they type "quit".
6. Reading, pt 2
Make a function that returns a list of all words in a file
"""
print("1. Reading") 
with open ("example.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())
file.close()
print("--------------------------")
print("2. Writing")
with open("my_file.txt", "w", encoding="utf-8") as file:
    file.write("Hello, world!")
with open("my_file.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())
file.close()
print("--------------------------")
print("3. Truncation?")
with open("my_file.txt", "w", encoding="utf-8") as file:
    file.write("Good Evening")
with open("my_file.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())
file.close()
print("--------------------------")
print("4. Appending")
user_input = input("What would you like to add?: ")
with open("my_file.txt", "a", encoding="utf-8") as file:
    file.write(f"\n{user_input}")
with open("my_file.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())
file.close()
print("--------------------------")
print("5. But now, with loops")

def game_action(word):
        with open("my_file.txt", "a", encoding="utf-8") as file:
            file.write(f"\n{word}")

        with open("my_file.txt", "r", encoding="utf-8") as file:
            for line in file:
                print(line.strip())
        return word
    
while True:
    word = input("What would you like to add, type 'quit' to exit?: ")
    if word.lower() == "quit":
        print("All done now")
        break
    else:
        game_action(word)

print("--------------------------")
print("6. Reading, pt 2")
word_list = []
with open("my_file.txt", "r", encoding="utf-8") as file:
    for line in file:
        new_word = line.split(" ")
        for word in new_word:
            word = word.strip()
            word_list.append(word)

print(word_list)
    
    
    
    

