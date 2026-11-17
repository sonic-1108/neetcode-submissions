class Solution:
    def jump(self, nums: List[int]) -> int:
        jump = 0
        current_end = 0
        farthest = 0
        for i in range(len(nums) - 1):
            farthest = max(farthest, nums[i] + i)
            if i == current_end:
                jump += 1
                current_end = farthest
                if current_end >= len(nums) - 1:
                    break
        return jump
        
