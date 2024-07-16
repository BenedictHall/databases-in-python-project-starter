from lib.account_repository import AccountRepository
from lib.account import Account

"""
When we call AccountRepository.all
We get a list of Account objects reflecting the seed data.
"""
def test_get_all_records(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = AccountRepository(db_connection)

    accounts = repository.all()

    assert accounts == [
        Account(1, 'Fake_guy_1', 'fake1@gmail.com'),
        Account(2, 'Fake_guy_2', 'fake2@gmail.com')
    ]

"""
When we call AccountRepository.find
We get a single Account object reflecting the seed data.
"""
def test_get_single_record(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = AccountRepository(db_connection)

    account = repository.find(2)
    assert account == Account(2, 'Fake_guy_2', 'fake2@gmail.com')

"""
When we call AccountRepository.create
We get a new record in the database.
"""
def test_create_record(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = AccountRepository(db_connection)

    repository.create(Account(None, 'funnyman', 'funnyman@gmail.com'))

    result = repository.all()
    assert result == [
        Account(1, 'Fake_guy_1', 'fake1@gmail.com'),
        Account(2, 'Fake_guy_2', 'fake2@gmail.com'),
        Account(3, 'funnyman', 'funnyman@gmail.com')
    ]

"""
When we call AccountRepository.delete
We remove a record from the database.
"""
def test_delete_record(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = AccountRepository(db_connection)
    repository.delete(2)

    result = repository.all()
    assert result == [
        Account(1, 'Fake_guy_1', 'fake1@gmail.com'),
    ]
