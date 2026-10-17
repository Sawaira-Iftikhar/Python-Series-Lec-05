# Python-Series-Lec-05


## 📚 Topics Covered
| # | Topic | Status |
|---|-------|:------:|
| 1 | `for` Loop Basics & `range()` Function | ✅ |
| 2 | `while` Loop Basics & Infinite Loop Prevention | ✅ |
| 3 | Looping Through Lists (Index-based & Direct) | ✅ |
| 4 | Looping Through Tuples & Unpacking in Loops | ✅ |
| 5 | Loop Control Statements (`break`, `continue`, `pass`) | ✅ |
| 6 | Nested Loops & `enumerate()` / `zip()` | ✅ |



## 📂 Practice Files

| File | Topics | Questions |
|------|--------|:---------:|
| [01_loops_basics.py](01_loops_basics.py) | `for` Loop, `while` Loop, `range()` | 07 |
| [02_loops_with_collections.py](02_loops_with_collections.py) | Looping Through Lists & Tuples, Unpacking | 10 |
| [02_loops_with_collections.py](03_loop_control_and_nested.py) | `break`, `continue`, `pass`, Nested Loops, `enumerate()`, `zip()` | 07 |
| [04_challenge.py](04_challenge.py) | ALL Topics Mixed (Boss Level) | 10 |

## 💡 Quick Cheat Sheet (Lecture 5 Highlights) 

<details>
<summary><b>Click to expand quick revision notes</b></summary>

<br>

### 1. Loop Types at a Glance

| Feature | `for` Loop | `while` Loop |
|---------|-----------|-------------|
| Use When | You know how many iterations | You don't know; condition-based |
| Syntax | `for item in iterable:` | `while condition:` |
| Risk | Almost none | Infinite loop if condition never becomes `False` |
| Best For | Lists, Tuples, Strings, Ranges | User input, counters, game loops |

### 2. `range()` Function

```python
range(stop)           # 0 to stop-1
range(start, stop)    # start to stop-1
range(start, stop, step)  # with step size

list(range(5))        # [0, 1, 2, 3, 4]
list(range(2, 8))     # [2, 3, 4, 5, 6, 7]
list(range(0, 10, 2)) # [0, 2, 4, 6, 8]
list(range(5, 0, -1)) # [5, 4, 3, 2, 1]
```
### 3. Looping Through Lists & Tuples

```python
fruits = ["apple", "banana", "cherry"]

# Direct iteration (Pythonic ✅)
for fruit in fruits:
    print(fruit)

# Index-based iteration
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")

# With enumerate (Best for index + value)
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# Tuple unpacking in loop
pairs = [(1, "a"), (2, "b"), (3, "c")]
for num, letter in pairs:
    print(f"{num} -> {letter}")
```

### 4. Loop Control Statements

| Statement | What It Does |
|-----------|--------------|
| `break`   | Exist the loop immediately|
| `continue`| Skips the rest of the current iteration, jumps to next|
| `pass`    | Does nothing - acts as a placeholder|

### 5. enumerate() & zip()

```python 
# enumerate: gives index + value
for i, val in enumerate(["x", "y", "z"], start=1):
    print(f"{i}. {val}")  # 1. x  2. y  3. z

# zip: combines two iterables
names = ["Ali", "Sara"]
scores = [90, 95]
for name, score in zip(names, scores):
    print(f"{name}: {score}")
```
</details>

## 📅 Series Progress

- [ ] ** Lecture 01 — Basics, Data Types & Operators ✅
- [ ] **Lecture 02 — Strings, Slicing & Conditionals ✅
- [ ] ** Lecture 03 — Lists, Tuples & Methods ✅
- [ ] **Lecture 04 — Coming Soon ✅
- [ ] **Lecture 05 — Coming Soon 📍 (Current)
- [ ] **Lecture 06** — Coming Soon
- [ ] **Lecture 07** — Coming Soon
- [ ] **Lecture 08** — Coming Soon
- [ ] **Lecture 09** — Coming Soon