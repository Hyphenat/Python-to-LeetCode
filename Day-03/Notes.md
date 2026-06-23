# Day 3 - Python Strings

## Topics Covered

* Strings
* String Indexing
* Negative Indexing
* String Length
* String Traversal
* Character Counting
* Vowel Counting
* Uppercase and Lowercase Methods
* Reverse String
* Palindrome Check

## Files

* Day3.py
* QuestionsDay3.py

## What I Learned

* A string is a sequence of characters.
* String indexing starts from 0, just like lists.
* Negative indexing can access characters from the end of a string.
* `len()` returns the number of characters in a string.
* Strings can be traversed using loops.
* Characters can be counted using a counter variable and loops.
* The `in` operator can check if a character exists in a string.
* `.upper()` converts a string to uppercase.
* `.lower()` converts a string to lowercase.
* `[::-1]` can be used to reverse a string.
* A palindrome reads the same forwards and backwards.

## Examples Learned

### String Traversal

```python
word = "Python"

for ch in word:
    print(ch)
```

### Count Character

```python
word = "banana"

count = 0

for ch in word:
    if ch == "a":
        count += 1

print(count)
```

### Count Vowels

```python
word = "education"

count = 0

for ch in word:
    if ch in "aeiou":
        count += 1

print(count)
```

### Reverse String

```python
word = "hello"

print(word[::-1])
```

### Palindrome Check

```python
word = "level"

if word == word[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
```

## Study Time

2-3 Hours

## Next Goal

* Dictionaries (Hash Maps)
* Key-Value Pairs
* Dictionary Traversal
* Searching in Dictionaries
* Sets
* Set Operations
* Introduction to LeetCode Two Sum

## Milestone

Completed revision of:

* Variables
* Data Types
* Input / Output
* Operators
* If-Else
* Loops
* Functions
* Return Values
* Lists
* Strings

Ready to learn Dictionaries and start solving beginner LeetCode problems.
