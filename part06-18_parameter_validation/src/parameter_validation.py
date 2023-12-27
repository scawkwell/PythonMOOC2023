# Write your solution here
def new_person(name: str, age: int):
    if age < 0 or age > 150:
        raise ValueError
    if name == "" or len(name) > 40 or " " not in name:
        raise ValueError
    
    return (name, age)


if __name__ == "__main__":
    print(new_person("seancawkwell", 24))