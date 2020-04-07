import unittest
from unittest import mock

from post_youdao import *

class PostYoudaoTest(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_get_ts(self):
        get_ts=mock.Mock(return_value=' 1584685303386')
        self.assertEqual(' 1584685303386', get_ts())

    def test_get_salt(self):
        get_salt=mock.Mock(return_value="15846853033868")
        self.assertEqual('15846853033868',get_salt())

    def test_get_sign(self):
        self.assertEqual(' 6f8837aae52584ce632e1fb224b1f482',get_sign())

if __name__ == '__main__':
    unittest.main()
