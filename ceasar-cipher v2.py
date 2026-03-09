# Caesar Cipher Program

# File: caesar-cipher v2.py
# Author: Anya Polmear
# Copyright: Copyright 2026, Anya Polmear

print("Welcome to Caesar Cipher Program.")

user_name = input("what is your name? ").title()
print(f"(Hi {user_name}. I hope you enjoy encrypting and decrypting messages. ")
user_input = input("What letter would you like me to encrypt for you?: ")

user_output = ord(user_input)

print(f'The ASCII number for "{user_input}" is {user_output}')

