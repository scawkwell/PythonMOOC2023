# Write your solution here
def import_recipe(filename : str):
    recipe_list = []
    with open(filename) as file:
        for row in file:
            recipe_list.append(row.strip())

    recipe_book = {}

    new_item = True
    for item in recipe_list:
        if item == "":
            new_item = True
            continue
        
        if new_item:
            recipe_book[item] = []
            last_key = item
            new_item = False
            continue

        recipe_book[last_key].append(item)

    return recipe_book

def search_by_name(filename: str, search_term: str):
    recipe_book = import_recipe(filename)
    output = []
    for recipe in recipe_book:
        if search_term.lower() in recipe.lower():
            output.append(recipe)
    return output

def search_by_time(filename: str, prep_time: int):
    recipe_book = import_recipe(filename)
    output = []
    for recipe, prep_time_and_ingredients in recipe_book.items():
        if int(prep_time_and_ingredients[0]) <= prep_time:
            output.append(f"{recipe}, preparation time {int(prep_time_and_ingredients[0])} min")
    return output

def search_by_ingredient(filename: str, ingredient: str):
    recipe_book = import_recipe(filename)
    output = []
    for recipe, prep_time_and_ingredients in recipe_book.items():
        if ingredient in prep_time_and_ingredients[1:]:
            output.append(f"{recipe}, preparation time {int(prep_time_and_ingredients[0])} min")
    return output   


if __name__ == "__main__":
    search_by_name("recipes1.txt", "cake")
    print(search_by_time("recipes1.txt", 20))
    found_recipes = search_by_ingredient("recipes1.txt", "eggs")
    print(found_recipes)

