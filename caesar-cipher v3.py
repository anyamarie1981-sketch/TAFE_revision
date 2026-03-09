# Caesar Cipher Program

# File: Caesar-cipher v3.py
# Author: Anya Polmear
# Copyright: Copyright 2026, Anya Polmear

print("Welcome to Caesar Cipher Program.")
user_name = input("what is your name? ").title()
print(f"Hi {user_name}. I hope you enjoy encrypting and decrypting messages. ")

def is_letter(letter):    
    if letter.isalpha():
        return True
    # else:
        return False

def is_number(user_shift):
    user_shift = user_shift.strip()
    try:
        return int(user_shift)
    except ValueError:
        return None

def ascii_wrap(letter, user_shift):
    if "A" <= letter <= "Z":
        new_code = (ord(letter) - ord("A") + user_shift) % 26 + ord("A")
        new_char = chr(new_code)
        return new_char    
    elif "a" <= letter <= "z":
        new_code = (ord(letter) - ord("a") + user_shift) % 26 + ord("a")
        new_char = chr(new_code)
        return new_char
    else:
        return None
  
while True:
    letter = input("What letter would you like me to encrypt for you?: ")
    if is_letter(letter):
        user_output = ord(letter)
        break
    else:
        print('Please only use alphabet characters')
 
while True:
    user_shift_str = input("How far should I shift the ASCII code?: ")
    user_shift = is_number(user_shift_str)
    if user_shift is not None:
        user_output = ascii_wrap(letter, user_shift)
        break
    else:
        print('Only numeric characters please')

print(
    f'''
Thanks {user_name}.
Your encrypted message is:
Input: {letter}
Caesar Cipher: {user_output}'''
        )

