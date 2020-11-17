class Solution:
    def palindrome(self, string):
        from re import sub
        s = sub('[/w_]','',string.lower())
        return s == s[::-1]

import unittest
a = Solution()

class Test(unittest.TestCase):
    def test(self):
        # write the test case here
        self.assertEqual(a.palindrome('tacocat'), True)
    
    def test2(self):
        self.assertEqual(a.palindrome('racecar'), True)
    
    def test3(self):
        self.assertEqual(a.palindrome('palindrome'), False)

if __name__ == '__main__':
    unittest.main()