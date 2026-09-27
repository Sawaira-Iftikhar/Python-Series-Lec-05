"""
============================================
  LECTURE 5 - FILE 3: LOOP CONTROL & NESTED LOOPS
  Topics: break, continue, pass, Nested Loops,
          enumerate(), zip()
  Total Questions: 
============================================
"""

# ==========================================
#  PART A: break & continue 
# ==========================================

# Q1. break STATEMENT:
#     Given: numbers = [12, 45, 7, 23, 99, 34, 56, 8]
#     Use a for loop to find the FIRST number greater than 50.
#     Once found, print it and break out of the loop.

numbers = [12, 45, 7, 23, 99, 34, 56, 8]

i = 0

while i < len(numbers):
    if numbers[i] > 50:
        print(f"First number > 50: {numbers[i]}")
        break

    i += 1

