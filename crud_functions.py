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


def get_all_products():
    all_list = []
    select_all = cursor.execute('SELECT * FROM Products')
    for i in select_all:
        all_list.append(i)
    return all_list


if __name__ == '__main__':
    connection.commit()
    connection.close()
