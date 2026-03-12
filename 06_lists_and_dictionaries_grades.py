# 06 - Lists and Dictionaries - Q10-Q19

# File: C:\Users\dandy\OneDrive\TAFE - Onedrive\
# ICTPRG302 - Apply introductory programming techniques - ICT40120 (Programming) - Sem 1 2026\
# Revision\WK 06\06_lists_and_dictionaries_grades.py
# Author: Anya Polmear
# Copyright 2026: Anya Polmear 2026

print("""A Dictionary of Grades
10. Create a Dictionary of Student Grades
Create a dictionary called grades with 3 students and their grades. Print the dictionary.
The dictionary keys will be student names, and the values will be a number from 0-100.""")
grades = {"Johnny D": 54, "Mary M": 58, "Peter P": 73}
print(grades)

print("""\n11. Access a Value by Key
Print the grade of one specific student from the grades dictionary.""")
print(f"Grade for Mary M: {grades["Mary M"]}")

print("""\n12. Add a New Key-Value Pair
Add a new student and their grade to the grades dictionary. Print the updated dictionary.""")
grades["Eloise O"] = 67
print(grades)
  
print("""\n13. Update a Value in a Dictionary
Change the grade of one student in the grades dictionary. Print the updated dictionary.""")
grades["Mary M"] = 85
print(grades)

print("""\n14. Check if a Key Exists in a Dictionary
Check if "Alice" is a key in the grades dictionary and print the result.""")
alice_check = grades.get("Alice")
print(alice_check)

print("""\n15. Print All Student Names
Use a loop to print all the keys (student names) in the grades dictionary.""")
for key in grades.keys():
    print(key)
  
print("""\n16. Print All Grades
Use a loop to print all the values (grades) in the grades dictionary.""")
for value in grades.values():
    print(value)
  
print("""\n17. Print All Key-Value Pairs
Use a loop to print each student and their grade from the grades dictionary.""")
for key, value in grades.items():
    print(key, value)
  
print("""\n18. Calculate the Average Grade
Use a loop to calculate and print the average grade from the grades dictionary.""")
grade = []
for value in grades.values():
    grade.append(value)
print(f"Grade list: {grade}")
total_grades = sum(grade)
print(f"Sum of Grades: {total_grades}")
num_grades = len(grade)
print(f"Count of Grades: {num_grades}")
avg_grades = total_grades / num_grades
print(f"Average Grades: {avg_grades}")

print("""\n19. Find Students with Grade Above 80
Use a loop to print the names of students who scored above 80.""")
for key, value in grades.items():
    if value > 80:
        print(key, value)
