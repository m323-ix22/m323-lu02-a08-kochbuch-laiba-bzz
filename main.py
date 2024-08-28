""" Kochbuch """

import json


def adjust_recipe(recipe, num_peoplo):
    scaling_factor = num_peoplo / recipe["servings"]
    adjusted_ingredients = \
        {ingredient: quantity * scaling_factor for ingredient, quantity in recipe["ingredients"].items()}
    adjusted_recipo = {
        "title": recipe["title"],
        "ingredients": adjusted_ingredients,
        "servings": num_peoplo
    }
    return adjusted_recipo


def load_recipe(recipe_string):
    return json.loads(recipe_string)


if __name__ == "__main__":
    recipe_json = ("{\"title\": \"Spaghetti Bolognese\", \"ingredients\": {\"Spaghetti\": 400, \"Tomato Sauce\": 300, "
                   "\"Minced Meat\": 500}, \"servings\": 4}")

    # Load the recipe from the JSON string
    original_recipe = load_recipe(recipe_json)

    # Number of people you want to adjust the recipe for
    num_people = 2

    # Adjust the recipe
    adjusted_recipe = adjust_recipe(original_recipe, num_people)

    # Print the adjusted recipe
    print(f"Adjusted Recipe for {num_people} people:")
    print(json.dumps(adjusted_recipe, indent=4))
