## test_database.py

import os
import sqlite3
import unittest
from typing import Any, Dict, Optional

from touch_typing_tutor.database import Database

class TestDatabase(unittest.TestCase):
    ## Setup and Teardown
    @classmethod
    def setUpClass(cls):
        cls.db = Database('test.db')

    @classmethod
    def tearDownClass(cls):
        cls.db.close()
        os.remove('test.db')

    ## Test Cases
    def test_create_tables(self):
        # Test if tables are created
        self.db.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = self.db.cursor.fetchall()
        self.assertIn(('users',), tables)
        self.assertIn(('progress',), tables)

    def test_insert_user(self):
        # Test if user insertion works
        self.db.insert_user('test_user', 'english')
        user = self.db.get_user('test_user')
        self.assertEqual(user, {'username': 'test_user', 'language': 'english'})

    def test_update_user(self):
        # Test if user update works
        self.db.update_user('test_user', 'spanish')
        user = self.db.get_user('test_user')
        self.assertEqual(user, {'username': 'test_user', 'language': 'spanish'})

    def test_get_user(self):
        # Test if get user works
        user = self.db.get_user('test_user')
        self.assertEqual(user, {'username': 'test_user', 'language': 'spanish'})

        # Test for non-existent user
        user = self.db.get_user('non_existent_user')
        self.assertIsNone(user)

    def test_insert_progress(self):
        # Test if progress insertion works
        self.db.insert_progress('test_user', 1, 'test_text', 'test_input')
        progress = self.db.get_progress('test_user')
        self.assertEqual(progress, [{'username': 'test_user', 'session_id': 1, 'text': 'test_text', 'input': 'test_input'}])

    def test_get_progress(self):
        # Test if get progress works
        progress = self.db.get_progress('test_user')
        self.assertEqual(progress, [{'username': 'test_user', 'session_id': 1, 'text': 'test_text', 'input': 'test_input'}])

        # Test for non-existent user
        progress = self.db.get_progress('non_existent_user')
        self.assertEqual(progress, [])

    def test_close(self):
        # Test if close works
        db = Database('test_close.db')
        db.close()
        with self.assertRaises(sqlite3.ProgrammingError):
            db.cursor.execute("SELECT * FROM users")

if __name__ == "__main__":
    unittest.main()
