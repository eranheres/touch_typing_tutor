## session.py

import curses
import random
import string
from typing import Dict
from user import User
from database import Database

class Session:
    def __init__(self, user: User):
        self.text: str = ""
        self.input: str = ""
        self.user: User = user
        self.db = Database()

    def generate_text(self):
        # For simplicity, we generate random text. In a real-world application, we would use a more sophisticated method.
        # The text generation could be improved to generate text based on the user's language.
        if self.user.language == 'English':
            self.text = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=100))
        else:
            # Add code here to generate text in other languages
            pass

    def get_input(self):
        # Initialize the curses library
        stdscr = curses.initscr()

        # Print the generated text
        stdscr.addstr(0, 0, self.text)

        # Get user input
        self.input = stdscr.getstr(1, 0, len(self.text)).decode('utf-8')

        # End the curses library
        curses.endwin()

    def end_session(self):
        # Save the session data to the user's progress
        session_id = len(self.user.progress) + 1
        self.user.progress[session_id] = {'text': self.text, 'input': self.input}

        # Save the user's progress to the database
        self.user.save_progress()
