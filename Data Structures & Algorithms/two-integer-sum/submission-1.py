class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        dif = 0
        for i in range(len(nums)):
            dif = target - nums[i]
            for j in range(i+1,len(nums)):
                if nums[j] == dif:
                    result.append(i)
                    result.append(j)
                    return result
