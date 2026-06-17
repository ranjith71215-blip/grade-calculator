# ==================================================
# STUDENT GRADE CALCULATOR
# Week 2 Project
# Author: Ranjith kumar G
# ==================================================

# Function to calculate grade
def calculate_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"


# Function to provide comments
def get_comment(grade):
    if grade == "A":
        return "Excellent! Outstanding performance."
    elif grade == "B":
        return "Very Good! You're doing well."
    elif grade == "C":
        return "Good Job! Keep improving."
    elif grade == "D":
        return "Needs Improvement. Work harder."
    else:
        return "Poor Performance. Seek extra help."


# Function to validate marks
def get_valid_mark(subject):
    while True:
        try:
            mark = float(input(f"{subject}: "))

            if 0 <= mark <= 100:
                return mark
            else:
                print("Marks must be between 0 and 100.")

        except ValueError:
            print("Invalid input! Enter a numeric value.")


# ---------------- MAIN PROGRAM ----------------

print("=" * 50)
print("      STUDENT GRADE CALCULATOR")
print("=" * 50)

# Validate number of students
while True:
    try:
        num_students = int(input("\nEnter number of students: "))

        if num_students > 0:
            break
        else:
            print("Please enter a positive number.")

    except ValueError:
        print("Invalid input! Enter a whole number.")

# List to store results
students = []

# Input student data
for i in range(num_students):

    print(f"\n=== STUDENT {i + 1} ===")

    name = input("Student name: ")

    print("Enter marks (0-100):")

    math = get_valid_mark("Math")
    science = get_valid_mark("Science")
    english = get_valid_mark("English")

    average = (math + science + english) / 3

    grade = calculate_grade(average)

    comment = get_comment(grade)

    student = {
        "name": name,
        "average": average,
        "grade": grade,
        "comment": comment
    }

    students.append(student)

# Calculate statistics
total_average = 0

highest_student = students[0]
lowest_student = students[0]

for student in students:

    total_average += student["average"]

    if student["average"] > highest_student["average"]:
        highest_student = student

    if student["average"] < lowest_student["average"]:
        lowest_student = student

class_average = total_average / len(students)

# Display Results
print("\n")
print("=" * 60)
print("                RESULTS SUMMARY")
print("=" * 60)

print(f"{'Name':20} | {'Avg':>5} | {'Grade':^5} | Comment")
print("-" * 60)

for student in students:

    print(
        f"{student['name']:20} | "
        f"{student['average']:5.1f} | "
        f"{student['grade']:^5} | "
        f"{student['comment']}"
    )

# Display Statistics
print("\n")
print("=" * 50)
print("            CLASS STATISTICS")
print("=" * 50)

print(f"Total Students : {len(students)}")
print(f"Class Average  : {class_average:.1f}")

print(
    f"Highest Average: "
    f"{highest_student['average']:.1f} "
    f"({highest_student['name']})"
)

print(
    f"Lowest Average : "
    f"{lowest_student['average']:.1f} "
    f"({lowest_student['name']})"
)

print("\n" + "=" * 50)
print("Thank you for using the Grade Calculator!")
print("=" * 50)