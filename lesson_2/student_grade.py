# Debugging steps:
# 1. Reproduce the error.
# 2. Determine the Boundries of the Error.
# 3. Trace the Code
# 4. Understand the problem well
# 5. Implement a fix
# 6. Test the Fix

def process_student(student_data):
    name = student_data.get('name')
    grade = student_data.get('grade')
    return (name, grade)

def average_grade(grades):
    total = sum(grades)
    average = total / len(grades)
    return average

students = [
    {'name': 'Alice', 'grade': 85},
    {'name': 'Bob'}, {'name': 'Jack', 'grade': 72},
    {'name': 'Jane', 'grade': 75},
]

def collect_grades(students):
    grades = []
    for student in students:
        name, grade = process_student(student)
        if grade != None:
            grades.append(grade)
    return grades

grades = collect_grades(students)
print(average_grade(grades))
