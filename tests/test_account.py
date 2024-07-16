from lib.account import Account

"""
Account constructs with an id, username, and email
"""
def test_account_constructs():
    account = Account(1, "Username1", "email1@gmail.com")
    assert account.id == 1
    assert account.username == "Username1"
    assert account.email == "email1@gmail.com"

"""
We can format accounts to strings nicely
"""
def test_accounts_format_nicely():
    account = Account(1, "Username1", "email1@gmail.com")
    assert str(account) == "Account(1, Username1, email1@gmail.com)"
