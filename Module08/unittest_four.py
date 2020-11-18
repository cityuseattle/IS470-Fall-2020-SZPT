import unittest


class Solution:
    def palindrome(self, string):
        from re import sub
        s = sub( '[/W_] ', '',string.lower())
        return s == s[::-1]


a = Solution()

class Test(unittest.TestCase):
    
    def test_first(self):
        self(a.palindrome(self,'Taco cat'))
    def test_second(self):
        self(a.palindrome(self,'rececar'))
    def test_third(self):
        self(a.palindrome(self,'Palindrome'))
        

if __name__ == '__main__':

    unittest.main()
