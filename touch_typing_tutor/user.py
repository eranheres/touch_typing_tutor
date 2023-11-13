## user.py

from typing import Dict
from database import Database

class User:
    def __init__(self, username: str, language: str = 'English'):
        self.username: str = username
        self.language: str = language
        self.progress: Dict = {}
        self.db = Database()

        user = self.db.get_user(self.username)
        if user is None:
            self.db.insert_user(self.username, self.language)
        else:
            self.language = user['language']

    def load_progress(self):
        self.progress = self.db.get_progress(self.username)

    def save_progress(self):
        for session_id, session in self.progress.items():
            text = session['text']
            input = session['input']
            self.db.insert_progress(self.username, session_id, text, input)
