"""
============================================
  LECTURE 5 - FILE 1: LOOPS BASICS
  Topics: for Loop, while Loop, range()
  Total Questions: 
============================================
"""

# ==========================================
#  PART A: for LOOP & range() 
# ==========================================

# Q1. BASIC for LOOP:
#     Use a for loop to print numbers from 1 to 5.
#     HINT: Use range()

for number in range(1, 6):
    print(number)

#----------------------------------------------------------------------------------------

# Q2. range() VARIATIONS:
#     Print the following sequences using range() inside a for loop:
#     a) 0 to 9
#     b) 5 to 15
#     c) Even numbers from 0 to 20
#     d) Odd numbers from 1 to 19
#     e) Countdown from 10 to 1

# 1.  0 to 9
for number in range(10):
    print(number, end=" ")

print()

# 2. 5 to 15
for number in range(5, 16):
    print(number, end=" ")

print()

# 3. Even numbers from 0 to 20
for number in range(0, 21, 2):
    print(number, end=" ")

print()

# 4. Odd numbers from 1 to 19
for number in range(1, 20, 2):
    print(number, end=" ")

print()

# 5. Countdown from 10 to 1
for number in range(10, 0, -1):
    print(number, end=" ")

#----------------------------------------------------------------------------------------

# Q3. for LOOP WITH STRINGS:
#     Given: word = "PYTHON"
#     a) Print each character on a new line using a for loop
#     b) Print each character with its index using range(len(word))


