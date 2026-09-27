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

# 3) Find the maximum price
maximum = prices[0]

for index in range(len(prices)):
    if prices[index] > maximum:
        maximum = prices[index]

print("Maximum: Rs.", maximum)

#-----------------------------------------------------------------------------------------

# Q3. BUILDING A NEW LIST FROM A LOOP:
#     Given: numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     a) Create a new list containing only EVEN numbers
#     b) Create a new list containing the SQUARE of each number
#     c) Create a new list containing numbers greater than 5
#     Print all three new lists.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1) Create a new list containing only EVEN numbers
evens = []

for number in numbers:
    if number % 2 == 0:
        evens.append(number)

print("Evens:", evens)

# 2) Create a new list containing the SQUARE of each number
squares = []

for number in numbers:
    squares.append(number ** 2)

print("Squares:", squares)

# 3) Create a new list containing numbers greater than 5
greater_than_5 = []

for number in numbers:
    if number > 5:
        greater_than_5.append(number)

print("Greater than 5:", greater_than_5)

#-----------------------------------------------------------------------------------------

# Q4. MODIFYING A LIST WHILE LOOPING:
#     Given: scores = [45, 82, 33, 91, 67, 55, 78]
#     Create a new list called `grades` by looping through scores:
#     - Score >= 90 → "A"
#     - Score >= 70 → "B"
#     - Score >= 50 → "C"
#     - Score < 50  → "F"
#     Print both lists side by side.


scores = [45, 82, 33, 91, 67, 55, 78]

# Create a new list to store grades
grades = []

# Loop through each score
for score in scores:
    # Score >= 90  "A"
    if score >= 90:
        grades.append("A")

    # Score >= 70  "B"
    elif score >= 70:
        grades.append("B")

   # Score >= 50  "C"
    elif score >= 50:
        grades.append("C")

   # Score < 50  "F"
    else:
        grades.append("F")

# Print both lists
print("Scores:", scores)
print("Grades:", grades)

#-----------------------------------------------------------------------------------------

# ==========================================
#  PART B: LOOPING THROUGH TUPLES 
# ==========================================

# Q5. BASIC TUPLE ITERATION:
#     Given: colors = ("red", "green", "blue", "yellow", "purple")
#     a) Print each color using a for loop
#     b) Print the length of each color name
#     c) Count how many colors have more than 4 characters

colors = ("red", "green", "blue", "yellow", "purple")

count = 0

for color in colors:
    print(f"{color} ({len(color)} letters)")

    if len(color) > 4:
        count += 1

print(f"Colors with > 4 chars: {count}")

#-----------------------------------------------------------------------------------------

# Q6. TUPLE UNPACKING IN LOOPS:
#     Given a list of tuples:
#     students = [("Ali", 85), ("Sara", 92), ("Hamza", 78), ("Fatima", 95)]
#
#     a) Use tuple unpacking in the for loop to print:
#        "Ali scored 85 marks"
#     b) Find the student with the highest score using a loop
#     c) Calculate the class average

students = [("Ali", 85), ("Sara", 92), ("Hamza", 78), ("Fatima", 95)]

highest_score = 0
topper = ""
total = 0

for name, score in students:
    print(f"{name} scored {score} marks")

    total += score

    if score > highest_score:
        highest_score = score
        topper = name

average = total / len(students)

print(f"Topper: {topper} with {highest_score} marks")
print(f"Class Average: {average}")

#-----------------------------------------------------------------------------------------

# Q7. NESTED TUPLE UNPACKING:
#     Given:
#     matrix_data = [
#         (1, (2, 3)),
#         (4, (5, 6)),
#         (7, (8, 9))
#     ]
#     Use nested unpacking in a for loop: for a, (b, c) in matrix_data:
#     Print: "a=1, b=2, c=3" for each row.

matrix_data = [
    (1, (2, 3)),
    (4, (5, 6)),
    (7, (8, 9))
]

for a, (b, c) in matrix_data:
    print(f"a={a}, b={b}, c={c}")

#-----------------------------------------------------------------------------------------

# ==========================================
#  PART C: MIXED COLLECTION LOOPS 
# ==========================================

# Q8. LOOPING THROUGH A LIST OF MIXED TYPES:
#     Given:  [10, "hello", 3.14, True, [1, 2], (3, 4)]
#     Loop through and print each item with its data type.
#     Use an if condition to print ONLY the numeric values (int and float).


mixed = [10, "hello", 3.14, True, [1, 2], (3, 4)]

for item in mixed:
    print(f"{item} --- {type(item)}")

print("--- Numeric values only ---")

for item in mixed:
    if isinstance(item, (int, float)) and not isinstance(item, bool):
        print(item)

#-----------------------------------------------------------------------------------------

# Q9. CREATING A DICTIONARY FROM TWO LISTS USING A LOOP:
#     Given:
#     keys = ["name", "age", "city", "role"]
#     values = ["Zainab", 24, "Lahore", "Developer"]
#
#     Create a dictionary by looping through both lists using range(len(keys)).
#     Print the resulting dictionary.

keys = ["name", "age", "city", "role"]
values = ["Zainab", 24, "Lahore", "Developer"]

# Create a dictionary by matching each key with its value
result = {}

for i in range(len(keys)):
    result[keys[i]] = values[i]

print(result)

#------------------------------------------------------------------------------------------

# Q10. FLATTENING A LIST OF LISTS:
#      Given:  [[1, 2, 3], [4, 5], [6, 7, 8, 9], [10]]
#      Use a nested for loop to flatten this into a single list:
#      flat = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#      Print the flattened list and its length.

nested_lists = [[1, 2, 3], [4, 5], [6, 7, 8, 9], [10]]

flat = []
