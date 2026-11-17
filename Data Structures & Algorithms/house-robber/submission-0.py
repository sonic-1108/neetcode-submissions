class Solution:
    def rob(self, nums: List[int]) -> int:
        first = 0
        second = 0
        for i in range(len(nums)):
            current = max(second, first + nums[i])
            first = second
            second = current
        return second