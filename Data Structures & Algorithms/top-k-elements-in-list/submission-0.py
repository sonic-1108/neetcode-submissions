class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = {}
        final = []
        for i in nums:
            if i not in result:
                result[i] = 1
            else:
                result[i] += 1
        final = sorted(result, key = result.get, reverse = True)
        return final[:k]