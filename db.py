import sqlite3

DATABASE_NAME = "betting_bot.db"

def db_connect():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn

def initialize_db():
    conn = db_connect()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                      (id INTEGER PRIMARY KEY, balance INTEGER)''')
    conn.commit()
    conn.close()

def update_balance(user_id, amount):
    conn = db_connect()
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO users (id, balance)
                      VALUES (?, ?)
                      ON CONFLICT(id) DO UPDATE SET balance = balance + ?
                      WHERE id = ?''', (user_id, amount, amount, user_id))
    conn.commit()
    conn.close()

def get_balance(user_id):
    conn = db_connect()
    cursor = conn.cursor()
    cursor.execute('SELECT balance FROM users WHERE id = ?', (user_id,))
    balance = cursor.fetchone()
    conn.close()
    return balance[0] if balance else 0
