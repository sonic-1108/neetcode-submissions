class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not s or not t:
            return False
        result = {}
        for i in s:
            if i not in result:
                result[i] = 1
            else:
                result[i] += 1
        for j in t:
            if j not in result:
                return False
            if result[j] >= 1:
                result[j] -= 1
            else:
                return False
        for k in result.values():
            if k:
                return False

        return True