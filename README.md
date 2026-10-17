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