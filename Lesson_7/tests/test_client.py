import sys
import unittest
from unittest.mock import patch
from Lesson_7.messenger import client


class TestClientActualWork(unittest.TestCase):

    @patch.object(sys, 'argv', ['client.py', '-p', 8000, '-a', '127.0.0.1'])
    def test_run_func_with_actual_params_ip_address(self):
        self.assertEqual(client.ip_address_verify_func(sys.argv), '127.0.0.1')

    @patch.object(sys, 'argv', ['client.py', '-p', 8000, '-a', '127.0.0.1'])
    def test_run_func_with_actual_params_port(self):
        self.assertEqual(client.port_verify_func(sys.argv), 8000)

    """ я не понимаю что значит эта ошибка, во время исключения произошло еще одно исключение
        в гугле нет аналогичных случаев, а на занятии наверное не записали в учебный план"""

    @patch.object(sys, 'argv', ['client.py', '-p', 8000])
    def test_run_func_without_actual_params_ip_address(self):
        self.assertRaises(IndexError, client.ip_address_verify_func(sys.argv))

    @patch.object(sys, 'argv', ['client.py', '-p', 80, '-a', '127.0.0.1'])
    def test_run_func_port_verify_without_actual_params_port(self):
        self.assertRaises(TypeError, client.port_verify_func)

    @patch.object(sys, 'argv', ['client.py', '-p', 80, '-a', '127.0.0.1'])
    def test_run_func_response_200_OK(self):
        self.assertEqual(client.connect_server("User", '127.0.0.1', 8000), '200 : OK')

    @patch.object(sys, 'argv', ['client.py', '-p', 80, '-a', '127.0.0.1'])
    def test_run_func_response_400_bad_request(self):
        self.assertEqual(client.connect_server("Guest", '127.0.0.1', 8000), '400 : Bad Request')


if __name__ == '__main__':
    unittest.main()
