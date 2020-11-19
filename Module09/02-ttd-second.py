import unittest # unit test f ramework

class Solution:
    def product_of_list(self, nums):
        if nums == 1:
            return 1
        return nums * (nums - 1)
        # product = 1
        # for i in range(len(nums)):
        #       product * nums[i]
        # return product
        # OR
        # return reduce((lambda x,y:x*y), nums)
a = Solution
class Test (unittest. TestCase) :

    def test_product_of_elements(self):
        self.assertEqual(a.product_of_list(self, 10), 90)
        #self.assertEqual(a.product_of_list(self, [1,4,6]), 24)

    def test_with_zero_element(self):
        self.assertEqual(a.product_of_list(self, 0), 0)
        #self.assertEqual(a.product_of_list(self, [1,4,0]), 0)

if __name__ == '__main__' :

    unittest. main()
