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

#-----------------------------------------------------------------------------------------

# Q2. continue STATEMENT:
#     Given: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     Use a for loop to print only ODD numbers.
#     Skip even numbers using continue.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers:
    if number % 2 == 0:
        continue

print(number, end=" ")

#-----------------------------------------------------------------------------------------


# Q3. break IN while LOOP:
#     Simulate a search in a list of tuples:
#     [("Ali", "555-0101"), ("Sara", "555-0202"),
#                 ("Hamza", "555-0303"), ("Zainab", "555-0404")]
#
#     Search for "Hamza" using a while loop with an index counter.
#     When found, print the phone number and break.
#     If not found after checking all, print "Contact not found."

contacts = [
    ("Ali", "555-0101"),
    ("Sara", "555-0202"),
    ("Hamza", "555-0303"),
    ("Zainab", "555-0404")
]

i = 0
found = False

while i < len(contacts):
    name, phone = contacts[i]

    if name == "Hamza":
        print(f"Found Hamza: {phone}")
        found = True
        break

i += 1

if not found:
    print("Contact not found.")

#-----------------------------------------------------------------------------------------

# ==========================================
#  PART B: pass & NESTED LOOPS 
# ==========================================

# Q5. NESTED while LOOPS — Multiplication Table:
#     Print the multiplication table from 1 to 5 (each up to 5).
#     Use two nested for loops.

row = 1

