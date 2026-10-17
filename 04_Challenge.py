"""
============================================
  LECTURE 5 - FILE 4: BOSS CHALLENGE 
  Topics: ALL Loop Topics Combined
  Total Challenges: 
============================================

"""

# ==========================================
#  CHALLENGE 1: The Shopping Cart Processor 
#  Topics: for Loop, Lists, Tuples, break, continue, enumerate
# ==========================================

"""
You are building a checkout system for an online store.

Given Cart Items (list of tuples: name, price, quantity, is_available):
cart = [
    ("Wireless Mouse", 25.0, 2, True),
    ("USB Cable", 5.0, 3, True),
    ("Keyboard", 75.0, 1, False),      # Out of stock!
    ("Monitor Stand", 45.0, 1, True),
    ("Webcam", 60.0, 0, True),          # Quantity is 0!
    ("Headphones", 35.0, 2, True)
]

Budget limit: budget = 200.0

Tasks:
1. Loop through the cart using enumerate() and tuple unpacking.
2. Skip items that are NOT available (is_available == False) using continue.
   Print: "Skipping Keyboard — Out of stock!"
3. Skip items with quantity 0 using continue.
   Print: " Skipping Webcam — Quantity is 0!"
4. For valid items, calculate line total (price × quantity).
5. Keep a running total. If adding an item exceeds the budget,
   use break to stop and print: " Budget exceeded! Stopping at {item}."
6. Print a final receipt of all successfully added items.

"""


# tuples in list
cart = [
    ("Wireless Mouse", 25.0, 2, True),
    ("USB Cable", 5.0, 3, True),
    ("Keyboard", 75.0, 1, False),
    ("Monitor Stand", 45.0, 1, True),
    ("Webcam", 60.0, 0, True),
    ("Headphones", 35.0, 2, True)
]

budget = 200.0
total = 0.0
purchased_items = []

# Print section started form here
print("=" * 50)
print("             CHECKOUT PROCESSOR")
print("=" * 50)
print("Processing Cart...")
print("-" * 50)

item_number = 0

for index, (name, price, quantity, is_available) in enumerate(cart):

      if not is_available:
        print(f" Skipping {name} — Out of stock!")
        continue

      if quantity == 0:
        print(f" Skipping {name} — Quantity is 0!")
        continue

      line_total = price * quantity

      if total + line_total > budget:
        print(f" Budget exceeded! Stopping at {name}.")
        break
 
      total += line_total
      item_number += 1

      purchased_items.append((name, price, quantity, line_total))

      print(
        f"{item_number}. {name:<18} | "
        f"Qty: {quantity} | "
        f"${price:.2f} | "
        f"Line: ${line_total:.2f}"
     )

print("-" * 50)
print(" Receipt Summary:")
print(f"   Items purchased: {item_number}")
print(f"   Total: ${total:.2f}")
print(f"   Budget remaining: ${budget - total:.2f}")
print("=" * 50)

#-----------------------------------------------------------------------------------------``

# ==========================================
#  CHALLENGE 2: The Grade Analyzer & Ranker 
#  Topics: Nested Loops, Lists of Tuples, zip(), Sorting Logic
#  Difficulty: Hard
# ==========================================
 
"""
You are a teacher analyzing class performance across multiple subjects.

Given Student Data (list of tuples):
students = [
    ("Ali", (88, 76, 92)),      # (Math, Physics, CS)
    ("Sara", (95, 89, 97)),
    ("Hamza", (60, 55, 70)),
    ("Fatima", (78, 82, 85)),
    ("Zayd", (45, 50, 40))
]

subjects = ("Math", "Physics", "Computer Science")
passing_marks = 50

Tasks:
1. For each student, calculate:
   a) Total marks (sum of all subjects)
   b) Average marks
   c) Highest subject score
   d) Lowest subject score
2. Determine if the student PASSED or FAILED:
   - Pass: ALL subjects >= passing_marks
   - Fail: ANY subject < passing_marks
3. Find the class topper (highest average).
4. Find the subject with the highest class average using zip().
5. Print a detailed report card.

"""

students = [
    ("Ali", (88, 76, 92)),
    ("Sara", (95, 89, 97)),
    ("Hamza", (60, 55, 70)),
    ("Fatima", (78, 82, 85)),
    ("Zayd", (45, 50, 40))
]

subjects = ("Math", "Physics", "Computer Science")
passing_marks = 50

student_results = []
subject_marks = []

print("=" * 50)
print("           CLASS PERFORMANCE REPORT")
print("=" * 50)
print(f"{'Student':<12}{'Math':<6}{'Physics':<9}{'CS':<7}{'Total':<7}{'Avg':<6}Status")
print("-" * 65)

for name, marks in students:
    total = sum(marks)
    average = total / len(marks)
    highest = max(marks)
    lowest = min(marks)

    if all(mark >= passing_marks for mark in marks):
        status = "✅ PASS"
    else:
        status = "❌ FAIL"

    student_results.append((name, average))
    subject_marks.append(marks)