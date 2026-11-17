class Solution:
    def search(self, nums: List[int], target: int) -> int:
        result = {}
        for i in range(len(nums)):
            result[nums[i]] = i
        if target in result:
            return result[target]
        else:
            return -1