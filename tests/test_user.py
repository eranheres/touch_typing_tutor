## test_user.py

import unittest
from unittest.mock import MagicMock
from touch_typing_tutor.user import User

class TestUser(unittest.TestCase):

    ## Test User Initialization
    def test_user_init(self):
        mock_db = MagicMock()
        mock_db.get_user.return_value = None
        user = User('test_user', 'Spanish', mock_db)
        self.assertEqual(user.username, 'test_user')
        self.assertEqual(user.language, 'Spanish')
        self.assertEqual(user.progress, {})
        mock_db.get_user.assert_called_once_with('test_user')
        mock_db.insert_user.assert_called_once_with('test_user', 'Spanish')

    ## Test User Initialization with Existing User
    def test_user_init_existing(self):
        mock_db = MagicMock()
        mock_db.get_user.return_value = {'language': 'French'}
        user = User('test_user', 'Spanish', mock_db)
        self.assertEqual(user.username, 'test_user')
        self.assertEqual(user.language, 'French')
        self.assertEqual(user.progress, {})
        mock_db.get_user.assert_called_once_with('test_user')
        mock_db.insert_user.assert_not_called()

    ## Test Load Progress
    def test_load_progress(self):
        mock_db = MagicMock()
        mock_db.get_user.return_value = None
        mock_db.get_progress.return_value = {'session1': {'text': 'abc', 'input': 'abc'}}
        user = User('test_user', 'English', mock_db)
        user.load_progress()
        self.assertEqual(user.progress, {'session1': {'text': 'abc', 'input': 'abc'}})
        mock_db.get_progress.assert_called_once_with('test_user')

    ## Test Save Progress
    def test_save_progress(self):
        mock_db = MagicMock()
        mock_db.get_user.return_value = None
        user = User('test_user', 'English', mock_db)
        user.progress = {'session1': {'text': 'abc', 'input': 'abc'}}
        user.save_progress()
        mock_db.insert_progress.assert_called_once_with('test_user', 'session1', 'abc', 'abc')

if __name__ == '__main__':
    unittest.main()
