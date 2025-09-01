#Test.py
from main import findNum
import unittest

class TestfindNum(unittest.TestCase):
    def test_findNum(self):
        self.assertEqual(findNum("abcd1l"), [
            "a occurred 1 time's",
            "b occurred 1 time's",
            "c occurred 1 time's",
            "d occurred 1 time's",
            "1 occurred 1 time's",
            "l occurred 1 time's"
        ])

if __name__ == '__main__':
    unittest.main()
