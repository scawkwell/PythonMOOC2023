# For model solution see - https://tmc.mooc.fi/exercises/193527/solution


# Initialize variables to store statistics
total_points_list = []
grade_list = []

# Collect input from the user
while True:
    user_input = input("Exam points and exercises completed: ")

    # Check for an empty line to end input collection
    if user_input == "":
        break

    # Split the input into exam points and exercises completed
    exam_points, exercises = map(int, user_input.split())

    # Calculate exercise points
    exercise_points = min(exercises // 10, 10)

    # Calculate total points
    total_points = exam_points + exercise_points

    # Calculate the grade based on the total points
    if exam_points < 10:
        grade = 0
    elif 15 <= total_points <= 17:
        grade = 1
    elif 18 <= total_points <= 20:
        grade = 2
    elif 21 <= total_points <= 23:
        grade = 3
    elif 24 <= total_points <= 27:
        grade = 4
    elif 28 <= total_points <= 30:
        grade = 5
    else:
        grade = 0

    # Append data to the lists
    total_points_list.append(total_points)
    grade_list.append(grade)

# Calculate statistics
average_points = sum(total_points_list) / len(total_points_list)
pass_percentage = (sum(grade > 0 for grade in grade_list) / len(grade_list)) * 100

# Print statistics
print("Statistics:")
print(f"Points average: {average_points:.1f}")
print(f"Pass percentage: {pass_percentage:.1f}")
print("Grade distribution:")
for grade_bracket in range(5, -1, -1):
    count = grade_list.count(grade_bracket)
    print(f"  {grade_bracket}: {'*' * count}")