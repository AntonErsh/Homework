import sqlite3


connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

# for i in range(1, 11):
#     cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
#                    (f'User{i}', f'example{i}@gmail.com', f'{i * 10}', 1000))

# for i in range(1, 11, 2):
#     cursor.execute('UPDATE Users SET balance = ? WHERE username = ?', (500, f'User{i}'))

# for i in range(1, 11, 3):
#     cursor.execute(f'DELETE FROM Users WHERE username = ?', (f'User{i}', ))

# cursor.execute('SELECT username, email, age, balance FROM Users WHERE age != ?', (60, ))
# print_users = cursor.fetchall()

# cursor.execute('DELETE FROM Users WHERE id = ?', (6, ))

cursor.execute('SELECT COUNT (*) FROM Users')
total = cursor.fetchone()[0]

cursor.execute('SELECT SUM (balance) FROM Users')
total_balance = cursor.fetchone()[0]

cursor.execute('SELECT AVG (balance) FROM Users')
avg_balance = cursor.fetchone()[0]
avg_balance_or = total_balance // total
print(avg_balance)
print(avg_balance_or)

connection.commit()
connection.close()
