import unittest


class Solution:
    def palindrome(self, string):
        from re import sub
        s = sub( '[/W_] ', '',string.lower())
        return s == s[::-1]


a = Solution

class Test(unittest.TestCase):
    
    def test_first(self):
        self.assertEqual(a.palindrome(self,'Taco cat'), False)
    def test_second(self):
        self.assertEqual(a.palindrome(self,'rececar'), False)
    def test_third(self):
        self.assertEqual(a.palindrome(self,'Palindrome'), False)
        

if __name__ == '__main__':

    unittest.main()
