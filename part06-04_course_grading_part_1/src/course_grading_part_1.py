# write your solution here

if True:
    # this is never executed
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
else:
    # hard-coded input
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"

student_ids = {}

with open(student_info) as file:
    for line in file:
        row = line.strip().split(";")
        if row[0] == "id":
            continue
        student_ids[row[0]] = f"{row[1]} {row[2]}"

student_exercises = {}

with open(exercise_data) as file:
    for line in file:
        row = line.strip().split(";")
        if row[0] == "id":
            continue
        grades = [int(part) for part in row[1:]]
        student_exercises[row[0]] = grades


for id, name in student_ids.items():
    print(f"{name} {sum(student_exercises[id])}")
