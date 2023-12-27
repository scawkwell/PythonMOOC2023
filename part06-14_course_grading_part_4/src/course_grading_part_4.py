# write your solution here
def calculate_grade(points):
    boundaries = [14, 17, 20, 23, 27, float('inf')]
    for grade, boundary in enumerate(boundaries):
        if points <= boundary:
            return grade

def get_course_info(course_info : str):
    course_name_and_credits = [0, 0]
    with open(course_info) as file:
        for row_no, row in enumerate(file):
            course_name_and_credits[row_no] = row[row.find(": ") + 2 :].strip()
    return course_name_and_credits

def get_student_names(student_info : str):
    student_names = {}
    with open(student_info) as file:
        for row in file:
            split_row = row.strip().split(";")
            if split_row[0] == "id":
                continue
            student_names[split_row[0]] = f"{split_row[1]} {split_row[2]}"
    return student_names

def get_student_exercises(exercise_data : str):
    student_exercises = {}
    with open(exercise_data) as file:
        for row in file:
            split_row = row.strip().split(";")
            if split_row[0] == "id":
                continue
            grades = [int(grade) for grade in split_row[1:]]
            student_exercises[split_row[0]] = grades
    return student_exercises

def get_student_exams(exam_points_file : str):
    student_exams = {}
    with open(exam_points_file) as file:
        for row in file:
            split_row = row.split(";")
            if split_row[0] == "id":
                continue
            exams = [int(exam) for exam in split_row[1:]]
            student_exams[split_row[0]] = exams
    return student_exams

def calculate_student_points(student_names : dict, student_exercises : dict, student_exams : dict):
    student_points = {id : None for id in student_names}
    for id in student_points:
        exercise_points = sum(student_exercises[id])//4
        exam_points = sum(student_exams[id])
        total_points = exercise_points + exam_points
        student_points[id] = (exercise_points, exam_points, total_points)
    return student_points

def process_student_final_grades(student_names : dict, student_points : dict):
    student_final_grades = {id : None for id in student_names}
    for id in student_final_grades:
        grade = calculate_grade(student_points[id][2])
        student_final_grades[id] = grade
    return student_final_grades

def create_results_output(student_names : dict, student_exercises : dict, student_points : dict, student_final_grades : dict, course_name_and_credits : list):
    with open("results.txt", "w") as results:
        results.write(course_name_and_credits[0])
        results.write(", ")
        results.write(course_name_and_credits[1])
        results.write(" credits\n")
        results.write(f"{"="*38}\n")
        results.write(f"{"name":30}{"exec_nbr":10}{"exec_pts.":10}{"exm_pts.":10}{"tot_pts.":10}{"grade":10}\n")
        for id, name in student_names.items():
            results.write(f"{name:30}{sum(student_exercises[id]):<10}{student_points[id][0]:<10}{student_points[id][1]:<10}{student_points[id][2]:<10}{student_final_grades[id]}\n")

def create_results_file(student_names : dict, student_final_grades : dict):
    with open("results.csv", "w") as file:
        for id, name in student_names.items():
            file.write(f"{id};{name};{student_final_grades[id]}\n")


def main():
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"
    exam_points_file = "exam_points1.csv"
    course_info = "course1.txt"

    student_info = input("students1.csv")
    exercise_data = input("exercises1.csv")
    exam_points_file = input("exam_points1.csv")
    course_info = input("course1.txt")



    student_names = get_student_names(student_info)
    student_exercises = get_student_exercises(exercise_data)
    student_exams = get_student_exams(exam_points_file)
    student_points = calculate_student_points(student_names, student_exercises, student_exams)
    student_final_grades = process_student_final_grades(student_names, student_points)
    course_name_and_credits = get_course_info(course_info)
    create_results_output(student_names, student_exercises, student_points, student_final_grades, course_name_and_credits)
    create_results_file(student_names, student_final_grades)

    print("Results written to files results.txt and results.csv")


main()
