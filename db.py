import sqlite3

db_name = 'db.sqlite'

conn = None
cursor = None

def open():
    global conn, cursor
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

def close():
    cursor.close()
    conn.close()

def do(query):
    cursor.execute(query)
    conn.commit()

def create():
    open()

    do('''
        CREATE TABLE news (
        id INTEGER PRIMARY KEY,
        title VARCHAR,
        category VARCHAR,
        description VARCHAR,
        imgUrl VARCHAR
       )''')
    
    do('''
        CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        username VARCHAR,
        email VARCHAR,
        password VARCHAR,
        role VARCHAR
       )''')
    
    close()

def drop_table(table):
    open()
    do(f'DROP TABLE IF EXISTS {table}')

# create()
def add_news(title, description, imgUrl):
    open()
    cursor.execute('''INSERT INTO news (title, description, imgUrl) VALUES (?,?,?)''', [title, description, imgUrl])
    conn.commit()
    close()

def add_user(username, email, password, role):
    open()
    cursor.execute('''INSERT INTO users (username, email, password, role) VALUES (?,?,?,?)''', [username, email, password, role])
    conn.commit()
    close()

def show(table):
    open()
    cursor.execute(f'SELECT * FROM {table}')
    print(cursor.fetchall())
    close()

def get_all_news():
    open()
    cursor.execute(f'SELECT * FROM news')
    return cursor.fetchall()

def get_news_by_id(id):
    open()
    cursor.execute(f'SELECT * FROM news WHERE news.id == ?', [id])
    return cursor.fetchall()


# add_news("123123213213123",'123123','sadadwqeqwe')
show('news')
# print(get_news_by_id(2))
# drop_table('news')
# drop_table('users')
# create()
