# import sys
#
# sys.path.append('../lesson_3/')

import sys
import unittest
from unittest.mock import patch
from Lesson_3 import server


class TestServerActualWork(unittest.TestCase):

    @patch.object(sys, 'argv', ['server.py', '-p', 80])
    def test_raise_value_error_fail_port(self):
        self.assertRaises(ValueError, server.main)

    @patch.object(sys, 'argv', ['server.py', '-p'])
    def test_raise_index_error_fail_port(self):
        self.assertRaises(IndexError, server.main)

    @patch.object(sys, 'argv', ['server.py', 'default'])
    def test_run_server_default_params(self):
        self.assertEqual(server.run_server_with_default_params(), 'default')

    @patch.object(sys, 'argv', ['server.py', '-p', 8000, '-a', '127.0.0.1'])
    def test_all_params_OK(self):
        self.assertEqual(server.main(), 'ok')


if __name__ == '__main__':
    unittest.main()
