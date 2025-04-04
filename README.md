# 🧠 Data Structures & Algorithms Project

This project includes Python implementations and algorithms for working with linked lists, stacks, binary trees, and expression parsing/evaluation. It is based on starter code and is meant to demonstrate key data structure operations and algorithmic problem solving.

## 📂 Files Overview

### ✅ `lrlist.py`
- **`MinAndMaxAlgo`**: Implements a single-pass algorithm to compute the minimum and maximum values of a list using a custom linked list implementation.

### ✅ `stack.py`
- **`LRStack`**: A stack implementation using the `LRList` as the underlying structure.
  - `__init__`
  - `push`
  - `pop`
  - `top`
  - `is_empty`
  - `size`
  - `__str__`, `__repr__`

### ✅ `bitree.py`
- **`PrefixToString`**: Converts a binary expression tree to a prefix (function-call style) string.
- **`PostfixToString`**: Converts a binary expression tree to a postfix (Reverse Polish Notation) string.

### ✅ `dijkstra.py`
- **`tokenize`**: Fixed to properly split expressions into tokens.
- **`to_rpn`**: Implements Dijkstra’s Shunting-Yard algorithm to convert infix expressions to postfix.
- **`eval_rpn`**: Evaluates a postfix expression using a left-to-right evaluation algorithm.

## ⚙️ Requirements

- Python 3.x
- PyCharm (recommended IDE)
- No external dependencies

## 📌 How to Run

1. Open the project folder in PyCharm or your preferred Python IDE.
2. Make sure `lrlist.py`, `stack.py`, `bitree.py`, and `dijkstra.py` are all in the same directory.
3. Run and test functions individually or using doctests provided in the files.

## 🧪 Testing

Doctests are provided in the code. You can run them by executing:
```bash
python -m doctest -v <filename>.py
