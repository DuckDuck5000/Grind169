class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        countP = Counter(p)
        left = 0
        countS = Counter()
        nP = len(p)
        output = []
        for i in range(0, len(s)):
            
            countS[s[i]] += 1
            if i >= nP-1:
                if countS == countP: output.append(left)
                countS[s[left]] -= 1
                if countS[s[left]] == 0: del countS[s[left]]
                left += 1
        return output
            
