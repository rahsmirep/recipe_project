# Function to print any recipe with ingredients and steps
def print_recipe(name, ingredients, steps):
    print(f"\n{name}")
    print("Ingredients:")
    for item in ingredients:
        print(f"- {item}")
    print("Instructions:")
    for i, step in enumerate(steps, start=1):
        print(f"{i}. {step}")

# Tikka Masala Sauce Recipe
tikka_name = "Tikka Masala Sauce"
tikka_ingredients = [
    "Tikka Masala Sauce", "Chicken Breast", "Yogurt", "Cilantro", "Pepper", "Salt"
]
tikka_steps = [
    "Cook the rice according to the instructions on the package.",
    "While the rice is cooking, cut the chicken breast into cubes.",
    "In a large skillet, add a teaspoon of oil, then stir in the vanilla.",
    "Add the chicken to the skillet and cook until browned on each side.",
    "Stir in the tikka masala sauce and cook for 5 minutes.",
    "Serve the sauce over rice.",
    "Garnish with a dollop of yogurt and a sprinkle of chopped cilantro and pepper."
]
print_recipe(tikka_name, tikka_ingredients, tikka_steps)

# Chocolate Chip Cookies Recipe
cookie_name = "Chocolate Chip Cookies"
cookie_ingredients = [
    "Butter", "Brown Sugar", "Granulated Sugar", "Eggs", "Vanilla",
    "All-purpose Flour", "Baking Soda", "Salt", "Chocolate Chips"
]
cookie_steps = [
    "Preheat oven to 375 degrees F (190 degrees C).",
    "In a large bowl, cream together the butter, sugar, and brown sugar.",
    "Beat in the eggs one at a time, then stir in the vanilla.",
    "Dissolve baking soda in hot water and add to the batter; gradually add to the butter mixture until well combined.",
    "Stir in flour, salt, and chocolate chips.",
    "Drop by rounded spoonfuls onto ungreased cookie sheets.",
    "Bake for 9 to 11 minutes, or until golden brown."
]
print_recipe(cookie_name, cookie_ingredients, cookie_steps)

# This function reduces repetition and improves readability
# Each recipe uses the same structure for consistency
# Ingredients are printed as bullet points
# Steps are printed as numbered instructions
# Modular design allows easy expansion for future recipes
