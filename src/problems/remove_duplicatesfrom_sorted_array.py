# 26. Remove Duplicates from Sorted Array

from typing import List


class RemoveDuplicatesfromSortedArray:
    def test_case(self):
        print(__name__)
        self.removeDuplicates([1,1,2])
        self.removeDuplicates([0,0,1,1,1,2,2,3,3,4])
        return

    def removeDuplicates(self, nums: List[int]) -> int:
        print('----- start -----', nums)
        result = 0
        set_nums = set(nums)
        result = len(set_nums)
        print('result', result)
        return result
    