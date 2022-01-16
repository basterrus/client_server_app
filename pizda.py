import sys
import unittest
from unittest.mock import patch


def main():
    argv = sys.argv
    if str(argv[1]).lower() == 'default':
        # run_server_with_default_params()
        return 'default'
    else:
        # try:
        if '-p' in argv:
            port = int(argv[argv.index('-p') + 1])
        else:
            raise IndexError

        if 1024 <= port <= 65535:
            pass
        else:
            raise ValueError

        if '-a' in argv:
            ip_address = argv[argv.index('-a') + 1]
        else:
            raise IndexError




class TestSummary(unittest.TestCase):

    @patch.object(sys, 'argv', ['server.py', '-p', 80])
    def test_value_port_NOT_OK(self):
        self.assertRaises(ValueError, main), 'test_value_port_NOT_OK ----> OK'



if __name__ == '__main__':
    argv = ['my_app.py', '-p', 80]
    main()

