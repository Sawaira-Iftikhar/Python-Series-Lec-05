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

word = "PYTHON"

# 1. Print each character on a new line
for character in word:
    print(character)

print()

# 2. Print each character with its index
for index in range(len(word)):
    print(index, "->", word[index])

#----------------------------------------------------------------------------------------

# Q4. SUM & PRODUCT USING for LOOP:
#     a) Calculate the sum of numbers from 1 to 100 using a for loop
#     b) Calculate the factorial of 5 (5! = 5 × 4 × 3 × 2 × 1) using a for loop


# 1. Sum of numbers from 1 to 100
total = 0

for number in range(1, 101):
    total += number

print("Sum 1 to 100:", total)

# 2. Factorial of 5
factorial = 1

for number in range(1, 6):
    factorial *= number

print("5! =", factorial)

#----------------------------------------------------------------------------------------

# ==========================================
#  PART B: while LOOP 
# ==========================================

# Q5. BASIC while LOOP:
#     a) Print numbers from 1 to 5 using a while loop
#     b) Print a countdown from 5 to 1 using a while loop
#     c) Print "Hello!" exactly 3 times using a while loop

# 1) Print numbers from 1 to 5
number = 1

while number <= 5:
    print(number)
    number += 1

# 2) Countdown from 5 to 1
number = 5

while number >= 1:
    print(number)
    number -= 1

# 3) Print "Hello!" exactly 3 times
count = 1

while count <= 3:
    print("Hello!")
    count += 1

#----------------------------------------------------------------------------------------

# Q6. while LOOP WITH ACCUMULATOR:
#     a) Calculate the sum of digits of the number 12345 using a while loop.
#        HINT: Use % 10 to get the last digit and // 10 to remove it.
#     b) Count how many digits are in the number 987654 using a while loop.



# 1) Sum of digits of 12345
number = 12345
digit_sum = 0

while number > 0:
    digit = number % 10
    digit_sum += digit
    number //= 10

print("Sum of digits of 12345:", digit_sum)


# 2) Count digits in 987654
number = 987654
digit_count = 0

while number > 0:
    number //= 10
    digit_count += 1

print("Number of digits in 987654:", digit_count)

#----------------------------------------------------------------------------------------

# ==========================================
#  PART C: for vs while COMPARISON 
# ==========================================

