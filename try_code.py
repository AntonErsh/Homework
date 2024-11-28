import sqlite3


connection = sqlite3.connect('try_db.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER
)
''')

cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users (email)')

# cursor.execute('INSERT INTO Users (username, email, age) VALUES (?, ?, ?)', ('newuser', 'ex@mail.ru', '20'))

# cursor.execute('UPDATE Users SET age = ? WHERE username = ?', ('15', 'newuser'))

cursor.execute('DELETE FROM Users WHERE username = ?', ('newuser', ))

connection.commit()
connection.close()
