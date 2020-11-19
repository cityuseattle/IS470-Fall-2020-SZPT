import unittest

class Solution:
    def product_of_list(self, nums):
        product = 1
        for i in range(len(nums)):
            product *= nums[i]
        return product

a = Solution
class Test(unittest.TestCase):

    def test_product_of_elements(self):
        self.assertEqual(a.product_of_list(self,[1,3,5]),15)
    
    def test_with_zero_elements(self):
        self.assertEqual(a.product_of_list(self,[1,3,0]),0)

if __name__ == '__main__':
    unittest.main()