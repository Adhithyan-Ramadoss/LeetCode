from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # check if target is met by two elements, where elements are chosen as:
        # first element of list and all subsequent elements chosen one by one, repeat for the next element where the
        # only the elements greater than the current are considered for the second element
        # (since the paring with smaller number is already checked when looping through the earlier pairs).
        for idx, val in enumerate(nums):
            if target - val in nums[:idx]:
                return idx, nums[:idx].index(target - val)
            elif target - val in nums[idx+1:]:
                return idx, nums[idx+1:].index(target - val) + idx + 1


dummy = Solution()
print(dummy.twoSum(nums = [2,7,11,15], target = 9))  # [0,1]
print(dummy.twoSum(nums = [3,2,4], target = 6))  # [1,2]
print(dummy.twoSum(nums = [3,3], target = 6))  # [0,1]