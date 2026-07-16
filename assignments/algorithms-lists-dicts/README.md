# 📘 Assignment: Algorithms with Lists and Dictionaries

## 🎯 Objective

Build confidence with beginner-level algorithmic thinking by solving small Python problems using lists, dictionaries, loops, and conditionals.

## 📝 Tasks

### 🛠️ Find a Student Score

#### Description
Implement a function called `find_score(students, target_name)` that searches a list of dictionaries and returns the score for the matching student.

#### Requirements
Completed program should:

- Receive a list in this format: `[{"name": "Ana", "score": 88}, ...]`
- Use a loop to find the dictionary whose `name` matches `target_name`
- Return the student score when found
- Return `None` when the student is not found

### 🛠️ Count Number Frequency

#### Description
Implement a function called `count_frequency(numbers)` that counts how many times each number appears in a list.

#### Requirements
Completed program should:

- Receive a list of integers
- Return a dictionary where keys are numbers and values are counts
- Use a dictionary to update counts during a single loop
- Example: `[2, 1, 2, 3, 1, 2]` should return `{2: 3, 1: 2, 3: 1}`

### 🛠️ Sort by Score (Highest First)

#### Description
Implement a function called `sort_by_score(students)` that returns a new list of students sorted by score in descending order.

#### Requirements
Completed program should:

- Receive a list of dictionaries in this format: `[{"name": "Ana", "score": 88}, ...]`
- Return a new list sorted from highest score to lowest score
- Keep the original list unchanged
- Use Python sorting with an appropriate key
