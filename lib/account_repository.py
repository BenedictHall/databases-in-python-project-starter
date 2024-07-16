from lib.account import Account

class AccountRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM accounts')
        accounts = []
        for row in rows:
            item = Account(row['id'], row['username'], row['email'])
            accounts.append(item)
        return accounts
    
    def find(self, id):
        rows = self._connection.execute(
            'SELECT * FROM accounts WHERE id = %s', [id]
        )
        row = rows[0]
        return Account(row['id'], row['username'], row['email'])
    
    def create(self, account):
        self._connection.execute(
            'INSERT INTO accounts (username, email) VALUES (%s, %s)', [
                account.username, account.email])
        return None
    
    def delete(self, id):
        self._connection.execute(
            'DELETE FROM accounts WHERE id = %s', [id]
        )
        return None