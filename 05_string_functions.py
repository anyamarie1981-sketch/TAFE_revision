# 05 - String Functions

# File: C:\Users\dandy\OneDrive\TAFE - Onedrive\
# ICTPRG302 - Apply introductory programming techniques - ICT40120 (Programming) - Sem 1 2026\
# Revision\WK 05\05_string_functions.py
# Author: Anya Polmear
# Copyright 2026: Anya Polmear 2026

# Defined Function Start
def revision_activities():
    return """
Revision Activities
1. Length of a String
2. Capitalize a Sentence inc 2b: Usability question:
3. Convert to Uppercase
4. Convert to Lowercase
5. Replace a Word
6. Find a Substring
7. Strip Whitespace
8. Check if a Word is in a Sentence
9. Combine Two Strings
10. Print Each Character in Uppercase
11. Replace All Vowels with "*"
12. Find All Occurrences of a Letter

Extensions
13. Count Words in a Sentence
14. Strip and Capitalize Each Word
15. Reverse a Sentence
16. Check Palindrome & 16A. Challenge: Now try it without using reverse
17. Remove All Digits from a String
    """

        
def rev_1():
    print("1. Length of a String")
    # Ask the user for a word and print its length using len() .

    print("Ask the user for a word and print its length using len()")
    word = input("Please enter a word: ")
    print(f'{word} is {len(word)} long')
    
def rev_2():

    print("\n2. Capitalize a Sentence")
    # Ask the user for a sentence and print it with the first character
    #capitalized using capitalize() .

    print("Ask the user for a sentence and"
          "print it with the first character capitalized using capitalize()")
    sentence = input("Please enter sentence: ").capitalize()
    print(sentence)
    '''
    print("""This would not work in situation where a proper noun is used in the
    sentence.
    An example f this would be: Can I leave a message for Miss Jones?\n 
    if you use 'capitalize', the output would be: 
    Can I lease a message for miss jones.""")
    '''
def rev_3():    
    sentence = input("Please enter sentence: ")
    print("\n3. Convert to Uppercase")
    ##Ask the user for a sentence and print it in all uppercase letters using upper() 
    print(sentence.upper())
    
def rev_4():  
    print("\n4. Convert to Lowercase")
    ##Ask the user for a sentence and print it in all lowercase letters using lower() .

    sentence = input("Please enter sentence: ")
    print(sentence.lower())

def rev_5():     
    print("\n5. Replace a Word")
    # Write a script that starts with the phrase "JavaScript is simple to code with".
    # Then change out "JavaScript" with "Python" using replace() .
    
    text = "JavaScript is simple to code with"
    result = text.replace("JavaScript", "Python")
    print(text)
    print(result)
    
def rev_6(): 
    print("\n6. Find a Substring")
    # Ask the user for a sentence and find the position of the word "code" using find() .
    # If you cannot find the word "code", print out the message "I guess you had other things to
    # talk about"
    user_sentence = input("Write a sentence and maybe use the word 'code': ")
    code_find = user_sentence.find("code")
    
    if code_find < 0:
        print("I guess you had other things to talk about")
    else:
        print(code_find)

def rev_7():     
    print("\n7. Strip Whitespace")
    # Ask the user for a sentence with leading and trailing spaces and print it stripped using
    # strip() .
    user_sentence = input("Write a sentence with leading a trailing whitespaces: ").strip()
    print(user_sentence)

def rev_8():     
    print("\n8. Check if a Word is in a Sentence")
    # Ask the user for a sentence and a word, then check if the word is in the sentence using in .
    user_word = input("What is your magic word? ")
    user_sentence = input("Write a sentence that includes your magic word: ")
    if user_word in user_sentence:
        word_find = user_sentence.find(user_word)
        print(f"Found it at position {word_find}")
    else:
        print("not in here")

def rev_9(): 
    print("\n9. Combine Two Strings")
    # Write a function which takes two strings and combines them with a space in-between.
    string_1 = "How_long_is"
    string_2 = "a_piece_of_string?"
    print(string_1)
    print(string_2)
    print(string_1 + " " + string_2)
    
def rev_10():     
    print("\n10. Print Each Character in Uppercase")
    #Ask the user for a word and print each character individually in uppercase using a loop.
    user_word = input("What is your word: ")
    for letter in user_word:
        print(letter.upper())
    
    print("<><><><><><>")
    
    index = 0
    
    while index < len(user_word):
        print(user_word[index].upper())
        index += 1
        
def rev_11():    
    print("\n11. Replace All Vowels with '*' ")
    # Ask the user for a sentence and replace all vowels with "*".
    user_sentence = input("What is your sentence: ").lower()
    vowel = ["a","e","i","o","u"]
    
    edit_sentence = []
    for letter in user_sentence:
        if letter in vowel:
            edit_sentence.append("*")
        else:
            edit_sentence.append(letter)
    final_sentence = "".join(edit_sentence).capitalize()
    print(final_sentence)

def rev_12():     
    print("\n12. Find All Occurrences of a Letter")
    # Ask the user for a sentence and a letter, then print all positions where the letter appears, by
    # using a loop.
    user_letter = input("Enter a letter: ").lower()
    user_sentence = input("Enter a sentence: ").lower()
    
    letters = []
    index = 0
    
    while index < len(user_sentence):
        if user_sentence[index] == user_letter:
            letters.append(index)
        index += 1
    print(letters)
    
def rev_13():     
    print("\n13. Count Words in a Sentence")
    # Ask the user for a sentence and count how many words it contains using 
    # split() and len().
    
    user_sent = input("What is your sentence? ")
    split_sent = user_sent.split(" ")
    print(split_sent)
    sent_len = len(split_sent)
    print(sent_len)
    
    all_split_sent = len(user_sent.split(" "))
    print(all_split_sent)
            
def rev_14():             
    print("\n14. Strip and Capitalize Each Word")
    # Ask the user for a sentence and strip and capitalize each word using a loop.
    # Use the split() method.   
    
    user_sent = input("What is your sentence? ").strip()
    s_sent = user_sent.split(" ")
    l_sent = len(s_sent)
    print(s_sent)
    print(l_sent)
    
    initial = 0
    
    while initial < l_sent:
    
        for each_word in s_sent:
            print(each_word.capitalize())
            initial += 1
    
def rev_15():     
    print("\n15. Reverse a Sentence")
    # Ask the user for a sentence and print it in reverse using slicing. [:]   
    
    user_sent = input("What is your sentence? ").strip()
    rev_sent = user_sent[::-1]
    print(rev_sent)
    
    split_sent = user_sent.split(" ")
    rev_split_sent = split_sent[::-1]
    print(rev_split_sent)

def rev_16():     
    print("\n16 & 16A. Check Palindrome")
    # Write a function is_palindrome(word) that returns True if the word is a 
    # palindrome (and False if it is not).
    # If you did the first part by comparing the word with the reversed word, 
    # now try doing it by comparing the word letter by letter.
    
    word = input("What is your word for a palindrome check? ").strip()
    
    def is_palindrome(word):
        if word == word[::-1]:
            return True
        else:
            return False
    
    def is_palindrome_again(word):
        index = 0
        e_index = -1
        while index < len(word):
            if word[index] == word[e_index]:
                # print(word[index])
                index += 1
                e_index -= 1
            else:
                return False
        return True    
    
    print(is_palindrome(word))
    print(is_palindrome_again(word))
    
def rev_17():     
    print("\n17. Remove All Digits from a String")
    
    # Ask the user for a string and remove all digits using a loop and isdigit() . Once again,
    # you'll need an accumulator to build the new string.
    
    user_sent = input("Write whatever garbage you like here: ")
    
    index = 0
    not_digits = []
    digits = []
    
    while index < len(user_sent):
        for char in user_sent:
            if char.isdigit():
                digits.append(char)
            else:
                not_digits.append(char)
    #        print(char)
            index += 1
    
    print(f"These are digits: {"".join(digits)}")
    print(f"These are not digits: {"".join(not_digits)}")
# Defined Function End

# Create Dictionary
split_rev_activities = revision_activities().splitlines()
ques_only = []
for line in split_rev_activities:
    if line.strip()[:1].isdigit():
        ques_only.append(line)

activities_dic = {}
for line in ques_only: 
    left, right = line.split(".", 1)
    key = int(left.strip())
    
    value = f"rev_{key}"
    func = globals().get(value)
    if func is not None:
        activities_dic[key] = func
    else:
        activities_dic[key] = None

# for key, value in activities_dic.items():
#     print(key, value)

#End Dictionary

# Start Code
while True:
    print(revision_activities())
    try:
        user_question = int(input("Which question would you like? "))
        q_num = activities_dic.get(user_question)
        if callable(q_num):
            q_num()
        else:
            print("Question not found")
    except ValueError:
        print("Use integer numbers only")
        
    again = input("""Would you like to review another question? 
    Y to continue, L to see a list of questions, or any key to quit
    """).upper()
    if again == "Y":
        continue
    elif again == "L":
        print(revision_activities())
    else:
        break
    break
