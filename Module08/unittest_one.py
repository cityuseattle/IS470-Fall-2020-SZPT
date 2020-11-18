import unittest
class TestStringMethods(unittest.TestCase):
    def test__upper(self):
        self.assertEqual( 'foo'.upper(), 'FOO')
if __name__ == '__main__':
    unittest.main()
