import unittest
from two_sum import twosum
class twosumtestsuite (unittest.TestCase):
    def test_list_list_range_4(self):
        res = twosum ([2,5,1,7,],8)
        self.assertEqual(res,[2,3])
        
    def test_list_list_range_5(self):
        res = twosum ([2,5,1,7,6],7)
        self.assertEqual(res,[0,1])
        
    def test_list_list_range_6(self):
        res = twosum ([2,5,1,7,8,9],6)
        self.assertEqual(res,[1,2])

    def test_list_list_range_7(self):
        res = twosum ([2,5,1,7,6,9,0],13)
        self.assertEqual(res,[3,4])

    def test_list_list_range_8(self):
        res = twosum ([2,5,1,7,6,9,0,6],3)
        self.assertEqual(res,[0,2])

    def test_list_list_range_9(self):
        res = twosum ([22,53,1,7,6,11,0,66,8],15)
        self.assertEqual(res,[3,8])

    def test_list_list_range_10(self):
        res = twosum ([2,5,1,7,6,9,0,7,8,10],18)
        self.assertEqual(res,[8,9])

    def test_list_list_range_11(self):
        res = twosum ([2,5,1,7,6,9,0,6,8,10,11],21)
        self.assertEqual(res,[9,10])

    def test_list_list_range_12(self):
        res = twosum ([2,5,1,99,6,55,0,6,8,10,11,12],15)
        self.assertEqual(res,[1,9])
        


if __name__ == "__main__":
    unittest.main()
        


