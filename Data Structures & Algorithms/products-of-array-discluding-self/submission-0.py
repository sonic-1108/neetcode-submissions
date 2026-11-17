class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = 1
        n = len(nums)
        right = 1
        result = [1] * n
        for i in range(n):
            result[i] = left
            left *= nums[i]
        for j in range(n-1, -1, -1):
            result[j] *= right
            right *= nums[j]
        return result
