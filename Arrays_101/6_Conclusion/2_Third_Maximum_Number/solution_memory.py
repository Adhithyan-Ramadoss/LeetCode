from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first = second = third = float("-inf")
        for num in nums:
            if num in [first, second, third]:
                continue
            elif first < num:
                third, second, first = second, first, num
            elif (second < num):
                third, second = second, num
            elif third < num:
                third = num
        return third if not (third == float("-inf")) else first


dummy = Solution()
print(dummy.thirdMax([3,2,1]))
print(dummy.thirdMax([1,2]))
print(dummy.thirdMax([2,2,3,1]))
print(dummy.thirdMax([1,2,-2147483648]))
print(dummy.thirdMax([5,2,4,1,3,6,0]))