# Student Grade Calculator

### Author

Ranjith kumar G

---

## Project Description

The Student Grade Calculator is a Python program that allows users to enter marks for multiple students, calculate their average scores, assign grades, generate personalized comments, and display class statistics.

This project demonstrates the use of Python fundamentals such as:

* Variables and Data Types
* Functions
* Conditional Statements (`if`, `elif`, `else`)
* Loops (`for`, `while`)
* Lists and Dictionaries
* Exception Handling (`try-except`)
* Input Validation
* Statistical Calculations
* Formatted Output

---

## Features

### Grade Calculation

Grades are assigned based on the student's average score:

| Average Score | Grade |
| ------------- | ----- |
| 90 - 100      | A     |
| 80 - 89       | B     |
| 70 - 79       | C     |
| 60 - 69       | D     |
| Below 60      | F     |

### Input Validation

* Number of students must be positive.
* Marks must be between 0 and 100.
* Invalid inputs are handled using exception handling.

### Statistics

The program calculates:

* Total Students
* Class Average
* Highest Average
* Lowest Average

---

## Project Structure

```text
week2/
│
├── grade_calculator.py
├── test_students.txt
├── results_sample.txt
└── README.md
```

---

## How to Run

### Method 1: Run Normally

Open the terminal in VS Code and run:

```bash
python grade_calculator.py
```

Enter student information when prompted.

---

### Method 2: Run Using Test File

Use the provided test data file:

```bash
python grade_calculator.py < test_students.txt
```

---

## Sample Input

```text
5
Ranjith
85
92
88
Harsha
78
81
85
Bhowmik
95
90
98
Naman
67
72
70
Yatish
55
60
58
```

---

## Sample Output

```text
==================================================
            CLASS STATISTICS
==================================================
Total Students : 5
Class Average  : 78.3
Highest Average: 94.3 (Bhowmik)
Lowest Average : 57.7 (Yatish)
```

---

## Learning Outcomes

By completing this project, you will learn how to:

* Create and use functions
* Work with lists and dictionaries
* Use loops to process multiple records
* Validate user input
* Handle runtime errors
* Calculate averages and statistics
* Display formatted tables
* Build a complete Python console application

---
## Optimization Techniques

* Modular design using functions
* Single-pass loop for statistics calculation
* Reusable input validation function
* Dictionary-based student record storage
* Reduced code duplication through function reuse

## Technologies Used

* Python 3
* Visual Studio Code (VS Code)

---

## Conclusion

This project is a practical introduction to Python programming and combines several core programming concepts into one complete application. It serves as a strong foundation for more advanced projects involving file handling, databases, and graphical user interfaces.
