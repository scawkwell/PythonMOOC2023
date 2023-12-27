# write your solution here

if True:
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exam_points_file = input("Exam points: ")
else:
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"
    exam_points_file = "exam_points1.csv"

def calculate_grade(points):
    boundaries = [14, 17, 20, 23, 27, float('inf')]
    for grade, boundary in enumerate(boundaries):
        if points <= boundary:
            return grade

student_names = {}

with open(student_info) as file:
    for row in file:
        split_row = row.strip().split(";")
        if split_row[0] == "id":
            continue
        student_names[split_row[0]] = f"{split_row[1]} {split_row[2]}"

student_exercises = {}

with open(exercise_data) as file:
    for row in file:
        split_row = row.strip().split(";")
        if split_row[0] == "id":
            continue
        grades = [int(grade) for grade in split_row[1:]]
        student_exercises[split_row[0]] = grades

student_exams = {}

with open(exam_points_file) as file:
    for row in file:
        split_row = row.split(";")
        if split_row[0] == "id":
            continue
        exams = [int(exam) for exam in split_row[1:]]
        student_exams[split_row[0]] = exams


# Process the exercise and exam data:

student_final_grades = {id : None for id in student_names}

for id in student_final_grades:
    exercise_points = sum(student_exercises[id])//4
    exam_points = sum(student_exams[id])
    grade = calculate_grade(exercise_points + exam_points)
    
    
    student_final_grades[id] = grade



print()
for id, name in student_names.items():
    print(f"{name} {student_final_grades[id]}")


