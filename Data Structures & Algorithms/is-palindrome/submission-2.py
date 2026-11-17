class Solution:
    def isPalindrome(self, s: str) -> bool:
        hi = s.lower()
        i = 0
        check = hi.split()
        check = "".join(check)
        n = len(check)
        j = n - 1
        while i <= j:
            while i < j and not check[i].isalnum():
                i += 1
            while i < j and not check[j].isalnum():
                j -= 1
            if check[i] != check[j]:
                return False
            i += 1
            j -= 1
        return True 

