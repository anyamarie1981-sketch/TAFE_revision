# 06 - Lists and Dictionaries - Q20

# File: C:\Users\dandy\OneDrive\TAFE - Onedrive\
# ICTPRG302 - Apply introductory programming techniques - ICT40120 (Programming) - Sem 1 2026\
# Revision\WK 06\06_lists_and_dictionaries_extension.py
# Author: Anya Polmear
# Copyright 2026: Anya Polmear 2026

print("""
20. Create a Dictionary of Word Counts
Ask the user to enter a sentence. Create a dictionary where each word is a key and its value
is the number of times it appears.
""")


sentence_dic = {
    1: "The quick brown fox jumped over the lazy dog",
    2: "Rose rose to put rose roes on her rows of roses",
    3: "James while John had had had had had had had had had had had a better effect on the teacher"
    }
    
while True:
    try:
        select = int(input("Pick a sentence: 1, 2, or 3: "))
        user_sent = sentence_dic.get(select)
        if user_sent is not None:
            break
        else:
            print("Enter a valid input")
    except ValueError:
        print("Enter a valid input")


print(f"\n{user_sent}")

word_count = 1
index = 0
sentence = {}
user_sent_list = user_sent.lower().split(" ")
print(f"\n{user_sent_list}\n")

for index in user_sent_list:
    sentence[f"word_{word_count}"] = index
    word_count += 1

for key, value in sentence.items():
    print(key, value)
print("\n")
count_words = {}
for word in user_sent_list:
    count_words[word] = count_words.get(word, 0) + 1
for key, value in count_words.items():
    print(key, value)

