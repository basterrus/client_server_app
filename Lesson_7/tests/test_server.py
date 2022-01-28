import sys
import unittest
from unittest.mock import patch
from Lesson_7.messenger import server


class TestServerActualWork(unittest.TestCase):

    @patch.object(sys, 'argv', ['server.py', '-p', 8000, '-a', '127.0.0.1'])
    def test_run_func_with_actual_params_port(self):
        self.assertEqual(server.port_verify_func(sys.argv), 8000)

    @patch.object(sys, 'argv', ['server.py', '-p', 8000, '-a', '127.0.0.1'])
    def test_run_func_with_actual_params_ip_address(self):
        self.assertEqual(server.ip_address_verify_func(sys.argv), '127.0.0.1')

    @patch.object(sys, 'argv', ['server.py', '-p', 80, '-a', '127.0.0.1'])
    def test_run_func_port_verify_without_arguments(self):
        self.assertRaises(TypeError, server.port_verify_func)

    @patch.object(sys, 'argv', ['server.py', '-p', 80, '-a', '127.0.0.1'])
    def test_run_func_ip_address_verify_without_arguments(self):
        self.assertRaises(TypeError, server.ip_address_verify_func)

    @patch.object(sys, 'argv', ['server.py', '-p', 80, '-a', '127.0.0.1'])
    def test_run_func_value_error_port(self):
        self.assertRaises(TypeError, server.port_verify_func)

    @patch.object(sys, 'argv', ['server.py', '-p', 80, '-a'])
    def test_run_func_value_error_ip_address(self):
        self.assertRaises(TypeError, server.ip_address_verify_func)

    def test_server_socket_addr(self):
        self.assertEqual(self.s.getsockname(), ('127.0.0.1', 7777))


if __name__ == '__main__':
    unittest.main()
