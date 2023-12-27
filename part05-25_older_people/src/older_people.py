# Write your solution here

def older_people(people : list, year : int):
    older = []

    for person in people:
        if person[1] < year:
            older.append(person[0])

    return older



if __name__ == "__main__":
    p1 = ("asdf", 100)
    p2 = ("qwer", 2)
    p3 = ("tyui", 3)

    people = [p1, p2, p3]

    print(older_people(people, 22))