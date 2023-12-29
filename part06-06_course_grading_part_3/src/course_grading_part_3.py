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

student_points = {id : None for id in student_names}

for id in student_points:
    exercise_points = sum(student_exercises[id])//4
    exam_points = sum(student_exams[id])
    total_points = exercise_points + exam_points
    student_points[id] = (exercise_points, exam_points, total_points)


for id in student_final_grades:
    grade = calculate_grade(student_points[id][2])
    student_final_grades[id] = grade


print(f"{"name":30}{"exec_nbr":10}{"exec_pts.":10}{"exm_pts.":10}{"tot_pts.":10}{"grade":10}")

for id, name in student_names.items():
    print(f"{name:30}{sum(student_exercises[id]):<10}{student_points[id][0]:<10}{student_points[id][1]:<10}{student_points[id][2]:<10}{student_final_grades[id]}")
    

    
