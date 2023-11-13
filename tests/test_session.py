## test_session.py

import unittest
from unittest.mock import patch, MagicMock
from user import User
from session import Session

class TestSession(unittest.TestCase):

    ## Test Initialization
    def test_init(self):
        user = User('John', 'English')
        session = Session(user)
        self.assertEqual(session.user, user)
        self.assertIsInstance(session.db, Database)
        self.assertEqual(session.text, "")
        self.assertEqual(session.input, "")

    ## Test generate_text method
    @patch('session.random.choices', return_value=['a', 'b', 'c'])
    def test_generate_text_english(self, mock_choices):
        user = User('John', 'English')
        session = Session(user)
        session.generate_text()
        self.assertEqual(session.text, 'abc')
        mock_choices.assert_called_once_with(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=100)

    ## Test get_input method
    @patch('session.curses.initscr')
    @patch('session.curses.endwin')
    def test_get_input(self, mock_endwin, mock_initscr):
        user = User('John', 'English')
        session = Session(user)
        session.text = 'abc'
        mock_initscr.return_value.getstr.return_value.decode.return_value = 'abc'
        session.get_input()
        mock_initscr.assert_called_once()
        mock_initscr.return_value.addstr.assert_called_once_with(0, 0, 'abc')
        mock_initscr.return_value.getstr.assert_called_once_with(1, 0, len('abc'))
        mock_endwin.assert_called_once()
        self.assertEqual(session.input, 'abc')

    ## Test end_session method
    @patch.object(User, 'save_progress')
    def test_end_session(self, mock_save_progress):
        user = User('John', 'English')
        session = Session(user)
        session.text = 'abc'
        session.input = 'abc'
        session.end_session()
        self.assertEqual(user.progress[1], {'text': 'abc', 'input': 'abc'})
        mock_save_progress.assert_called_once()

if __name__ == '__main__':
    unittest.main()
