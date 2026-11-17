class Solution:
    def maxArea(self, heights: List[int]) -> int:
        current = 0
        left = 0
        n = len(heights)
        right = n - 1
        best = 0
        best = max(best, current)
        while left < right:
            current = (right - left) * min(heights[left], heights[right])
            best = max(best, current)
            if heights[left] < heights[right]:
                left += 1
            elif heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        return best
        



