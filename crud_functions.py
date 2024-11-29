import sqlite3

connection = sqlite3.connect('crud_func.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Products (
id INTEGER PRIMARY KEY,
title TEXT NOT NULL,
description TEXT,
price INT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INT PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INT NOT NULL,
balance INT NOT NULL
)
''')


def add_user(username: str, email: str, age: int) -> None:
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
                   (username, email, age, 1000))
    connection.commit()


def is_included(username: str) -> bool:
    check_user = cursor.execute('SELECT * FROM Users WHERE username = ?', (username, )).fetchone()
    connection.commit()
    if check_user:
        return True
    else:
        return False


def get_all_products() -> list:
    all_list = []
    select_all = cursor.execute('SELECT * FROM Products')
    for i in select_all:
        all_list.append(i)
    return all_list


if __name__ == '__main__':
    connection.commit()
    connection.close()
