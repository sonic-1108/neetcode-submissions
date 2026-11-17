class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for i in strs:
            n = sorted(i)
            key = ''.join(n)
            if key not in result:
                result[key] = []
            result[key].append(i)
        return list(result.values())