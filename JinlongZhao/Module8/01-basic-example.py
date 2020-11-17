import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
    
if __name__ == '__main__':
    unittest.main()

    def test_isupper(self):
        self.asserTrue('FOO'.isupper())
        self.asserFalse('Foo'.isupper())
    
    def test_split(self):
        s='hello world'
        self.asserEqual(s.split(),['hello','world'])
        # check that s.split fails when the separator is not a string
        with self.asserRaises(TypeError):
            s.split(2)