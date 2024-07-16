from lib.database_connection import DatabaseConnection
from lib.artist_repository import ArtistRepository
from lib.album_repository import AlbumRepository
""" from lib.recipe_repository import RecipeRepository
 """
""" 
# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/music_library.sql")

# Retrieve all artists
artist_repository = ArtistRepository(connection)
artists = artist_repository.all()

# List them out
for artist in artists:
    print(artist)

album_repository = AlbumRepository(connection)
albums = album_repository.all()

for album in albums:
    print(album)

connection.seed("seeds/recipes.sql")

recipe_repository = RecipeRepository(connection)
recipes = recipe_repository.all()

for recipe in recipes:
    print(recipe) """

class Application:
    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
        self._connection.seed('seeds/music_library.sql')
    
    def run(self):
        print('What would you like to do?\n1 - List all albums\n2 - List all artists\n')
        response = input("Enter your choice: ")
        if response == '1':
            repo = AlbumRepository(self._connection)
            albums = repo.all()
            for album in albums:
                print(f"{album.id}: {album.title}")
        elif response == '2':
            repo = ArtistRepository(self._connection)
            artists = repo.all()
            for artist in artists:
                print(f"{artist.id}: {artist.name}")
        else:
            print('Invalid response, please try again')

if __name__ == '__main__':
    app = Application()
    app.run()
