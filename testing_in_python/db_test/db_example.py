import sqlite3


class Database:
    """Simulates a basic user database."""

    def __init__(self):
        self.data = {}

    def add_user(self, user_id, name):
        if user_id in self.data:
            raise ValueError("User ID already exists.")
        self.data[user_id] = name

    def get_user(self, user_id):
        return self.data.get(user_id, None)

    def delete_user(self, user_id):
        if user_id in self.data:
            del self.data[user_id]
        else:
            raise ValueError("User ID does not exist.")


def save_user_to_db(name, age):
    """Saves a user to an SQLite database."""
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL
        )
    """)
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
    conn.commit()
    conn.close()
