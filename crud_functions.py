import sqlite3

connection = sqlite3.Connection('db_homework.db')
cursor = connection.cursor()

def initiate_db():
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS Products(
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT,
            price INT NOT NULL
            )
            ''')


def get_all_products():
    cursor.execute('SELECT * FROM Products')
    all_products = cursor.fetchall()
    return all_products


# initiate_db()

# cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)'
#                , ('Продукт 1', 'Ананас', 400))
# cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)'
#                , ('Продукт 2', 'Груша', 150))
# cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)'
#                , ('Продукт 3', 'Киви', 100))
# cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)'
#                , ('Продукт 4', 'Манго', 300))

# a = get_all_products()
# print(a)

connection.commit()
# connection.close()
