"""
============================================
  LECTURE 5 - FILE 2: LOOPS WITH LISTS & TUPLES
  Topics: Iterating Lists, Iterating Tuples,
          Tuple Unpacking in Loops
  Total Questions: 
============================================
"""

# ==========================================
#  PART A: LOOPING THROUGH LISTS 
# ==========================================

# Q1. DIRECT ITERATION:
#     Given:  ["apple", "banana", "cherry", "date", "elderberry"]
#     a) Print each fruit using a for loop (direct iteration)
#     b) Print each fruit in UPPERCASE
#     c) Print only fruits that have more than 5 characters


fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# 1) Print each fruit
for fruit in fruits:
    print(fruit)

print()

# 2) Print each fruit in uppercase
for fruit in fruits:
    print(fruit.upper())

print()
