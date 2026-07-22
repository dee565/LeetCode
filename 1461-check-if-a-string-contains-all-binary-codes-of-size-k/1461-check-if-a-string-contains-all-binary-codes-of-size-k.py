class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)
        if n < k:
            return False
        substrings = set()
        for i in range(k, n+1):
            substrings.add(s[i-k:i])
        return len(substrings) == (1 << k)