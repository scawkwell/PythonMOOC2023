def user_inputs():
    exam_points_and_exercises = []
    while True:
        user_input = input("Exam points and exercises completed: ")

        if user_input == "":
            break

        exam_points_and_exercises.append(user_input)

    return exam_points_and_exercises


def calculate_exercise_points(exercises):

    for boundary in range(10, 101, 10):
        if exercises == 100:
            return 10
        if exercises < boundary:
            return boundary // 10 - 1


def calculate_grade(exam_points, total_points):
    boundaries = [14, 17, 20, 23, 27, 30]

    if exam_points < 10:
        return 0

    for grade in range(6):
        if total_points <= boundaries[grade]:
            return grade


def print_statistics(grade_list, total_points_list):
    mean = float(sum(total_points_list)/len(total_points_list))
    pass_rate = float(sum(grade > 0 for grade in grade_list)/len(grade_list) * 100)

    print("Statistics:")
    print(f"Points average: {mean:.1f}")
    print(f"Pass percentage: {pass_rate:.1f}")
    print("Grade distribution: ")
    for grade_bracket in range(5, -1, -1):
        count = sum(grade == grade_bracket for grade in grade_list)
        print(f"  {grade_bracket}: {count * "*"}")


def process_data(exam_points_and_exercises):

    grade_list = []
    total_points_list = []

    for entry in exam_points_and_exercises:

        entry = entry.split()
        exam_points = int(entry[0])
        exercises = int(entry[1])

        exercise_points = calculate_exercise_points(exercises)
        total_points = exam_points + exercise_points
        grade = calculate_grade(exam_points, total_points)

        grade_list.append(grade)
        total_points_list.append(total_points)

    print_statistics(grade_list, total_points_list)



def main():
    data = user_inputs()
    process_data(data)


main()

