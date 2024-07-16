from lib.recipe import Recipe

"""
Recipe constructs with an id, name, cooking time, and rating
"""
def test_recipe_constructs():
    recipe = Recipe(1, "Test Recipe", 30, 3)
    assert recipe.id == 1
    assert recipe.name == "Test Recipe"
    assert recipe.cooking_time == 30
    assert recipe.rating == 3

"""
We can format recipes to strings nicely
"""
def test_recipes_format_nicely():
    recipe = Recipe(1, "Test Recipe", 30, 3)
    assert str(recipe) == "Recipe(1, Test Recipe, 30, 3)"

"""
We can compare two identical recipes and have them be equal
"""
def test_recipes_are_equal():
    recipe1 = Recipe(1, "Test Recipe", 30, 3)
    recipe2 = Recipe(1, "Test Recipe", 30, 3)
    assert recipe1 == recipe2