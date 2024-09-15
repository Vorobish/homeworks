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
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS Users(
                id INTEGER PRIMARY KEY,
                username TEXT NOT NULL,
                email TEXT NOT NULL,
                age INT NOT NULL,
                balance INT NOT NULL
                )
                ''')
    connection.commit()


def get_all_products():
    cursor.execute('SELECT * FROM Products')
    all_products = cursor.fetchall()
    return all_products


def is_include(username):
    check_user = cursor.execute('SELECT * FROM Users WHERE username = ?', (username, ))
    if check_user.fetchone() is None:
        connection.commit()
        return False
    else:
        connection.commit()
        return True


def add_users(username, email, age):
    if is_include(username) is False:
        cursor.execute(f'INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, 1000)',
                       (username, email, age))
    connection.commit()

# def get_all_products():
#     products_list = cursor.execute('SELECT * FROM Products')
#     message = ''
#     for product in products_list:
#         message += f'{product[0]} @ {product[1]} @ {product[2]} @ {product[3]} \n'
#     connection.commit()
#     return message

initiate_db()

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

# b = cursor.execute('SELECT * FROM Products')
# for i in b:
#     print(i)

# a = is_include('newuser')
# print(a)

# add_users('Ann', 'user@gmail.com', 25)

# cursor.execute('DROP TABLE Users')

connection.commit()
# connection.close()
