## test_statistics.py

import unittest
from unittest.mock import MagicMock, patch
from touch_typing_tutor.statistics import Statistics
from touch_typing_tutor.user import User
from touch_typing_tutor.session import Session

class TestStatistics(unittest.TestCase):

    ## Test Initialization
    def test_init(self):
        user = User("test_user")
        stats = Statistics(user)
        self.assertEqual(stats.user, user)
        self.assertEqual(stats.data, {})
        self.assertIsNotNone(stats.db)

    ## Test collect_data function
    @patch('touch_typing_tutor.statistics.Database.get_progress')
    def test_collect_data(self, mock_get_progress):
        user = User("test_user")
        stats = Statistics(user)
        session = Session(user)
        mock_data = [{'session_id': 1, 'text': 'test text', 'input': 'test input'}]
        mock_get_progress.return_value = mock_data
        stats.collect_data(session)
        self.assertEqual(stats.data, mock_data)

    ## Test display_data function
    @patch('builtins.print')
    def test_display_data(self, mock_print):
        user = User("test_user")
        stats = Statistics(user)
        session = Session(user)
        mock_data = [{'session_id': 1, 'text': 'test text', 'input': 'test input'}]
        stats.data = mock_data
        stats.display_data()
        calls = [call('Session ID: 1'), call('Text: test text'), call('Input: test input'), call('---------------------')]
        mock_print.assert_has_calls(calls)

if __name__ == '__main__':
    unittest.main()
