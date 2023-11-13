## statistics.py

from typing import Dict
from user import User
from session import Session
from database import Database

class Statistics:
    def __init__(self, user: User):
        self.user: User = user
        self.data: Dict = {}
        self.db = Database()

    def collect_data(self, session: Session):
        # Collect data from the session
        self.data = self.db.get_progress(self.user.username)

    def display_data(self):
        # Display the collected data
        # For simplicity, we just print the data. In a real-world application, we would use a more sophisticated method.
        for session in self.data:
            print(f"Session ID: {session['session_id']}")
            print(f"Text: {session['text']}")
            print(f"Input: {session['input']}")
            print("---------------------")
