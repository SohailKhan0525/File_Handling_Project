# 📁 File Handling Project (Python CLI)

A menu-driven Command-Line Interface (CLI) application built in Python that lets users **create**, **read**, and **delete** files directly from the terminal — with live directory listing on every action.

---

## 📌 Project Overview

**File:** `file_project.py`

A `while True` loop keeps the program running until the user chooses to quit. At each iteration the user picks an operation from a numbered menu, and the corresponding function is called.

**Menu options:**

```
**************************
Press '1' to create a file
Press '2' to read a file
Press '3' to delete a file
Press '4' to quit the program
**************************
```

---

## 🛠️ Technologies Used

| Tool / Module | Purpose |
|---------------|---------|
| Python 3 | Core programming language |
| `pathlib.Path` | Object-oriented path and file operations |
| `os.remove()` | Deleting files from the filesystem |
| `open()` built-in | Reading and writing file content |

---

## 🧠 What I Learned

### 1. Using `pathlib` for Path and File Operations

- **`Path('')`** creates a `Path` object pointing to the current working directory.
- **`path.rglob('*')`** recursively walks every file and folder inside a directory — much cleaner than nested `os.walk()` calls.
- **`p.exists()`** checks whether a path (file *or* directory) exists on disk before acting on it.
- **`p.is_file()`** narrows the check down to regular files, guarding against accidentally reading a directory name.

```python
path = Path('')
items = list(path.rglob('*'))     # recursive listing of all files & folders
p = Path(name)
if not p.exists():                # safe guard before creating
    ...
```

### 2. Working with the `open()` Built-in and Context Managers

- Opening a file with `open(p, 'w')` creates it (or overwrites it) for writing; `open(p, 'r')` opens it for reading.
- Using the **`with` statement** (context manager) ensures the file is automatically closed even if an error occurs — no need for a manual `f.close()`.

```python
with open(p, 'w') as fs:
    fs.write(data)   # write user input to the file

with open(p, 'r') as fs:
    data = fs.read() # read the full file content at once
```

### 3. Deleting Files with `os.remove()`

- `os.remove(name)` permanently removes the file at the given path.
- Always verify the file exists *and* is a regular file before calling `remove()` to avoid unexpected errors.

```python
import os
os.remove(name)
```

### 4. Building a Menu-Driven CLI with a `while True` Loop

- A **`while True`** loop combined with a **`break`** statement creates an infinite menu that exits only when the user explicitly chooses to quit.
- `if / elif / else` chains map each numeric choice to its handler function.

```python
while True:
    check = int(input("Enter your response: "))
    if check == 1:
        createfile()
    elif check == 2:
        readfile()
    elif check == 3:
        deletefile()
    elif check == 4:
        break          # exit the loop cleanly
    else:
        print(f"{check} is a/an invalid.")
```

### 5. Enumerating a List with `enumerate()`

- `enumerate(items)` pairs each item with a zero-based index, making it easy to print a numbered list without a manual counter variable.

```python
for i, item in enumerate(items):
    print(f"{i+1}: {item}")   # 1-based numbering for readability
```

### 6. Error Handling with `try / except`

- Wrapping risky operations (file I/O, user input conversion) in `try / except Exception as err` prevents the program from crashing unexpectedly.
- Catching `Exception` at the top level surfaces helpful error messages while keeping the program running.

```python
try:
    check = int(input("Enter your response: "))
except Exception as error:
    print(f"Please enter a valid number [{error}]")
```

### 7. f-Strings for Clean Output

- Python **f-strings** (`f"..."`) allow variables and expressions to be embedded directly inside string literals — more readable than `+` concatenation or `.format()`.

```python
print(f"{i+1}: {items}")
print(f"An error occured as {err}")
```

### 8. Organising Code into Functions

- Each operation (`readfileandfolder`, `createfile`, `readfile`, `deletefile`) is encapsulated in its own function — keeping the main loop short and each concern isolated.
- `readfileandfolder()` is called at the start of every operation so the user always sees the current state of the directory.

---

## ▶️ How to Run

1. Make sure **Python 3** is installed on your system.

2. Clone or download this repository, then run:

```bash
python file_project.py
```

3. Follow the on-screen numbered menu to create, read, or delete files.

---

## 📜 Feature Summary

| Feature | Supported |
|---|---|
| Recursive directory listing | ✅ |
| Create a file with custom content | ✅ |
| Read and display file content | ✅ |
| Delete a file | ✅ |
| Prevent overwriting existing files | ✅ |
| Error handling & input validation | ✅ |