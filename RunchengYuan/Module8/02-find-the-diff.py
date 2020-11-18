import unittest

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_list = sorted(s)
        t_list = sorted(t)
        for i in range(len(s_list)):
            if s_list[i] != t_list[i]:
                return t_list[i]
        return t_list[-1]

a = Solution
class Test(unittest.TestCase):

    def test_diff_at_end(self):
        self.assertEqual(a.findTheDifference(self,"abcd","abcde"),"e")

    def test_diff_at_begin(self):
        self.assertEqual(a.findTheDifference(self,"bcd", "abcd"), "a")

    def test_diff_at_2nd_to_last(self):
        self.assertEqual(a.findTheDifference(self,"bce","bcde"),"d")
    
    def test_empty(self):
        self.assertEqual(a.findTheDifference(self,"", "a"), "a")

if __name__ == '__main__':
    unittest.main()