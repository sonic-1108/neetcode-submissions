class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for i in range(n)]
        output = ''
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j]:
                    if j - i <= 2 or dp[i+1][j-1] == True:
                        dp[i][j] = True
                if dp[i][j] and j - i + 1 > len(output):
                    output = s[i:j + 1]
        return output