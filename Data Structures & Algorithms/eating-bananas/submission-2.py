class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        if h < n:
            return None
        if h == n:
            return max(piles)
        left = 1
        right = max(piles)
        while left < right:
            hours = 0
            mid = (left + right) // 2 
            for pile in piles:
                hours += (pile + mid - 1) // mid
            if hours > h:
                left = mid + 1
            else:
                right = mid
        return left





