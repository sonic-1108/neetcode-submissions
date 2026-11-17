class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def rob_line(houses):
            first = 0
            second = 0
            for i in houses:
                current = max(second, first + i)
                first = second
                second = current
            return second
        return max(rob_line(nums[:len(nums)-1]), rob_line(nums[1:]))
        
            