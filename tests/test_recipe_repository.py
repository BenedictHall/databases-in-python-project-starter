from lib.recipe_repository import RecipeRepository
from lib.recipe import Recipe

"""
When we call RecipeRepository.all()
we get a list of Recipe objects reflecting the seed data
"""
def test_get_all_records(db_connection):
    db_connection.seed("seeds/recipes.sql")
    repository = RecipeRepository(db_connection)

    recipes = repository.all()

    assert recipes == [
        Recipe(1, 'Meatloaf', 60, 1),
        Recipe(2, 'Spaghetti', 20, 4),
        Recipe(3, 'Sandwich', 5, 3),
        Recipe(4, 'Lasagna', 120, 5)
    ]

"""
When we call RecipeRepository#find
We get a single Recipe object reflecting the seed data.
"""
def test_get_single_record(db_connection):
    db_connection.seed("seeds/recipes.sql")
    repository = RecipeRepository(db_connection)

    recipe = repository.find(3)
    assert recipe == Recipe(3, 'Sandwich', 5, 3)

"""
When we call RecipeRepository#create
We get a new record in the database.
"""
def test_create_record(db_connection):
    db_connection.seed("seeds/recipes.sql")
    repository = RecipeRepository(db_connection)

    repository.create(Recipe(None, 'Omelette', 10, 4))

    result = repository.all()
    assert result == [
        Recipe(1, 'Meatloaf', 60, 1),
        Recipe(2, 'Spaghetti', 20, 4),
        Recipe(3, 'Sandwich', 5, 3),
        Recipe(4, 'Lasagna', 120, 5),
        Recipe(5, 'Omelette', 10, 4)
    ]

"""
When we call RecipeRepository#delete
We remove a record from the database.
"""
def test_delete_record(db_connection):
    db_connection.seed("seeds/recipes.sql")
    repository = RecipeRepository(db_connection)
    repository.delete(3)

    result = repository.all()
    assert result == [
        Recipe(1, 'Meatloaf', 60, 1),
        Recipe(2, 'Spaghetti', 20, 4),
        Recipe(4, 'Lasagna', 120, 5)
    ]
