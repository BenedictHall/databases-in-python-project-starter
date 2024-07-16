from lib.post_repository import PostRepository
from lib.post import Post

"""
When we call PostRepository.all
We get a list of Post objects reflecting the seed data.
"""
def test_get_all_records(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)

    posts = repository.all()

    assert posts == [
        Post(1, 'new game', 'wow guys new game', 18, 1),
        Post(2, 'new movie', 'wow guys new movie', 45, 1),
        Post(3, 'new anime', 'wow guys new anime', 28, 2),
        Post(4, 'new sport', 'wow guys new sport', 8, 2)
    ]

"""
When we call PostRepository.find
We get a single Post object reflecting the seed data.
"""
def test_get_single_record(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)

    post = repository.find(2)
    assert post == Post(2, 'new movie', 'wow guys new movie', 45, 1)

"""
When we call PostRepository.create
We get a new record in the database.
"""
def test_create_record(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)

    repository.create(Post(None, 'funny cats', 'lots of em', 400, 2))

    result = repository.all()
    assert result == [
        Post(1, 'new game', 'wow guys new game', 18, 1),
        Post(2, 'new movie', 'wow guys new movie', 45, 1),
        Post(3, 'new anime', 'wow guys new anime', 28, 2),
        Post(4, 'new sport', 'wow guys new sport', 8, 2),
        Post(5, 'funny cats', 'lots of em', 400, 2)
    ]

"""
When we call PostRepository.delete
We remove a record from the database.
"""
def test_delete_record(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)
    repository.delete(2)

    result = repository.all()
    assert result == [
        Post(1, 'new game', 'wow guys new game', 18, 1),
        Post(3, 'new anime', 'wow guys new anime', 28, 2),
        Post(4, 'new sport', 'wow guys new sport', 8, 2)
    ]
