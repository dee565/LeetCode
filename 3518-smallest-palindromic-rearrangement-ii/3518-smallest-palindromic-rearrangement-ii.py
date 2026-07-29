class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        n = len(s)
        m = n // 2
        c = [0] * 26
        for ch in s[:m]:
            c[ord(ch) - 97] += 1
        ans = []
        tot = 0
        perm = 1
        tmp = 0
        for i in range(25,-1,-1):
            tot += c[i]
            perm *= math.comb(tot, c[i])
            if perm >= k:
                tmp = perm
                for valid in range(0,i):
                    ans.extend([chr(valid + 97)] * c[valid])
                    c[valid] = 0
                break
        else:
            if perm < k:
                return ""
        if tmp:
            perm = tmp
        m -= len(ans)
        l = m
        start = 0
        for _ in range(m):
            for i in range(start,26):
                if not c[i]:
                    continue
                tmp = perm * c[i] // l
                if tmp < k:
                    start = i + 1
                    k -= tmp
                    continue
                else:
                    ans.append(chr(i + 97))
                    c[i] -= 1
                    perm = tmp
                    l -= 1
                    start = 0
                    break
        left = "".join(ans)
        return left + (s[n // 2] if n % 2 else "") + left[::-1]
        