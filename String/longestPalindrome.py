class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        letters = Counter(s)
        res = count = 0
        for i in letters.values():
            
            if i > 1:
                if i % 2 == 0:
                    res += i
                else:
                    res += i -1
                    count += 1
            else:
                count += 1
        if count > 0:
            res += 1
        return res