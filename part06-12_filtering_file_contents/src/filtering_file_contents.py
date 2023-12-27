# Write your solution here

def filter_solutions():
    solutions = import_solutions()
    filter_to_lists(solutions)

def import_solutions():
    with open("solutions.csv") as file:
        output = []
        for row in file:
            parts = row.strip().split(";")
            parts[2] = int(parts[2])
            output.append(parts)
    return output

def solution_is_correct(problem : list):
    question = problem[1]
    if "+" in question:
        solution = question.split("+")
        solution = int(solution[0]) + int(solution[1])
    else:
        solution = question.split("-")
        solution = int(solution[0]) - int(solution[1])

    return solution == problem[2]

def filter_to_lists(problems : list):
    correct_solutions = []
    incorrect_solutions = []

    for problem in problems:
        if solution_is_correct(problem):
            correct_solutions.append(problem)
        else:
            incorrect_solutions.append(problem)

    write_to_file(correct_solutions, "correct.csv")
    write_to_file(incorrect_solutions, "incorrect.csv")

def write_to_file(solutions : list, file_name : str):
    with open(file_name, "w") as file:
        for solution in solutions:
            line = f"{solution[0]};{solution[1]};{solution[2]}\n"
            file.write(line)

