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

cart = [
    ("Wireless Mouse", 25.0, 2, True),
    ("USB Cable", 5.0, 3, True),
    ("Keyboard", 75.0, 1, False),
    ("Monitor Stand", 45.0, 1, True),
    ("Webcam", 60.0, 0, True),
    ("Headphones", 35.0, 2, True)
]

