class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        result = 0
        for n in seen:
            if n - 1 not in seen:
                current = n
                length = 1
                while current + 1 in seen:
                    current += 1
                    length += 1
                result = max(result,length)
        return result
            

