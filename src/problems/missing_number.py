# 268. Missing Number

from typing import List


class MissingNumber:
    def test_case(self):
        print(__name__)
        self.missingNumber([3,0,1])
        self.missingNumber([0,1])
        self.missingNumber([9,6,4,2,3,5,7,0,1])
        return

    def missingNumber(self, nums: List[int]) -> int:
        print('----- start -----', nums)
        correct_total = 0
        for index in range(1, (len(nums) + 1)):
            correct_total += index
        result = correct_total - sum(nums)
        print('result', result)
        return result
    