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

# 3) Print fruits with more than 5 characters
for fruit in fruits:
    if len(fruit) > 5:
        print(fruit)

#-----------------------------------------------------------------------------------------

# Q2. INDEX-BASED ITERATION:
#     Given: prices = [120, 350, 80, 500, 200]
#     Use range(len(prices)) to:
#     a) Print each price with its index: "Item 0: Rs.120"
#     b) Calculate the total of all prices
#     c) Find the maximum price using a loop (don't use max())


prices = [120, 350, 80, 500, 200]

# 1) Print each price with its index
for index in range(len(prices)):
    print(f"Item {index}: Rs.{prices[index]}")

# 2) Calculate the total
total = 0

for index in range(len(prices)):
    total += prices[index]

print("Total: Rs.", total)