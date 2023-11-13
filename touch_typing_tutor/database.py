## database.py

import sqlite3
from typing import Any, Dict, Optional

class Database:
    def __init__(self, db_name: str = 'touch_typing_tutor.db'):
        try:
            self.conn = sqlite3.connect(db_name)
            self.cursor = self.conn.cursor()
            self.create_tables()
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")

    def create_tables(self):
        try:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    username TEXT PRIMARY KEY,
                    language TEXT
                )
            """)
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS progress (
                    username TEXT,
                    session_id INTEGER,
                    text TEXT,
                    input TEXT,
                    FOREIGN KEY(username) REFERENCES users(username)
                )
            """)
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error creating tables: {e}")

    def insert_user(self, username: str, language: str):
        try:
            self.cursor.execute("""
                INSERT INTO users (username, language) VALUES (?, ?)
            """, (username, language))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error inserting user: {e}")

    def update_user(self, username: str, language: str):
        try:
            self.cursor.execute("""
                UPDATE users SET language = ? WHERE username = ?
            """, (language, username))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error updating user: {e}")

    def get_user(self, username: str) -> Optional[Dict[str, Any]]:
        try:
            self.cursor.execute("""
                SELECT * FROM users WHERE username = ?
            """, (username,))
            row = self.cursor.fetchone()
            if row is None:
                return None
            return {'username': row[0], 'language': row[1]}
        except sqlite3.Error as e:
            print(f"Error getting user: {e}")

    def insert_progress(self, username: str, session_id: int, text: str, input: str):
        try:
            self.cursor.execute("""
                INSERT INTO progress (username, session_id, text, input) VALUES (?, ?, ?, ?)
            """, (username, session_id, text, input))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error inserting progress: {e}")

    def get_progress(self, username: str) -> Dict[str, Any]:
        try:
            self.cursor.execute("""
                SELECT * FROM progress WHERE username = ?
            """, (username,))
            rows = self.cursor.fetchall()
            return [{'username': row[0], 'session_id': row[1], 'text': row[2], 'input': row[3]} for row in rows]
        except sqlite3.Error as e:
            print(f"Error getting progress: {e}")

    def close(self):
        try:
            self.conn.close()
        except sqlite3.Error as e:
            print(f"Error closing database connection: {e}")
