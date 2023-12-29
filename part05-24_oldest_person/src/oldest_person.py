# Write your solution here
def oldest_person(people : list):
    oldest = people[0][1]
    oldest_indx = 0
    for index, person in enumerate(people):
        if person[1] < oldest:
            oldest = person[1]
            oldest_indx = index

    return people[oldest_indx][0]


if __name__ == "__main__":
    p1 = ("asdf", 100)
    p2 = ("qwer", 2)
    p3 = ("tyui", 3)

    people = [p1, p2, p3]

    print(oldest_person(people))
