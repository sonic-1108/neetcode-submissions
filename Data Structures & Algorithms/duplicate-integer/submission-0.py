class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        result = {}
        found = False
        for i in nums:
            if i not in result:
                result[i] = 1
            else:
                result[i] += 1
                found = True
        return found