import sqlite3
from django.db import models
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

class UserModel:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

    @classmethod
    def create_table(cls):
        conn = sqlite3.connect(str(BASE_DIR / 'databases' / 'users.db'))
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT,
                email TEXT
            )
        ''')
        conn.commit()
        conn.close()

    def insert(self):
        conn = sqlite3.connect(str(BASE_DIR / 'databases' / 'users.db'))
        cursor = conn.cursor()
        try:
            cursor.execute('INSERT INTO users (id, name, email) VALUES (?, ?, ?)', 
                           (self.id, self.name, self.email))
            conn.commit()
            return True
        except sqlite3.IntegrityError:
            print(f"Duplicate or invalid entry for user {self.id}")
            return False
        finally:
            conn.close()

class ProductModel:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    @classmethod
    def create_table(cls):
        conn = sqlite3.connect(str(BASE_DIR / 'databases' / 'products.db'))
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY,
                name TEXT,
                price REAL
            )
        ''')
        conn.commit()
        conn.close()

    def insert(self):
        conn = sqlite3.connect(str(BASE_DIR / 'databases' / 'products.db'))
        cursor = conn.cursor()
        try:
            # Validate price is non-negative
            if self.price < 0:
                print(f"Invalid price for product {self.id}")
                return False
            
            cursor.execute('INSERT INTO products (id, name, price) VALUES (?, ?, ?)', 
                           (self.id, self.name, self.price))
            conn.commit()
            return True
        except sqlite3.IntegrityError:
            print(f"Duplicate entry for product {self.id}")
            return False
        finally:
            conn.close()

class OrderModel:
    def __init__(self, id, user_id, product_id, quantity):
        self.id = id
        self.user_id = user_id
        self.product_id = product_id
        self.quantity = quantity

    @classmethod
    def create_table(cls):
        conn = sqlite3.connect(str(BASE_DIR / 'databases' / 'orders.db'))
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY,
                user_id INTEGER,
                product_id INTEGER,
                quantity INTEGER
            )
        ''')
        conn.commit()
        conn.close()

    def insert(self):
        conn = sqlite3.connect(str(BASE_DIR / 'databases' / 'orders.db'))
        cursor = conn.cursor()
        try:
            # Validate quantity is non-negative
            if self.quantity < 0:
                print(f"Invalid quantity for order {self.id}")
                return False
            
            cursor.execute('INSERT INTO orders (id, user_id, product_id, quantity) VALUES (?, ?, ?, ?)', 
                           (self.id, self.user_id, self.product_id, self.quantity))
            conn.commit()
            return True
        except sqlite3.IntegrityError:
            print(f"Duplicate or invalid entry for order {self.id}")
            return False
        finally:
            conn.close()