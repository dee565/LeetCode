class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        digits="123456789"
        ans=[]
        minlen=len(str(low))
        maxlen=len(str(high))
        for length in range(minlen,maxlen+1):
            for start in range(10-length):
                num = int(digits[start:start+length])
                if low <= num <= high:
                    ans.append(num)
        return ans
        