from typing import List

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        
        dic={}      
        for i,word in enumerate(words):
            dic[word]=i
            
        result=set()
        for i,word in enumerate(words):
            for j in range(len(word)+1):
                prefix=word[:j]
                rev_pre=prefix[::-1]
                pal=word+rev_pre
                if rev_pre in dic and dic[rev_pre]!=i and pal==pal[::-1]:
                    result.add((i,dic[rev_pre]))
                
                suffix=word[j:]
                rev_suff=suffix[::-1]
                pal=rev_suff+word
                
                if rev_suff in dic and dic[rev_suff]!=i and pal==pal[::-1]:
                    result.add((dic[rev_suff],i))
                    
                    
        return list(result)
    
# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1: Basic case
    words1 = ["abcd", "dcba", "lls", "s", "sssll"]
    print(f"Test Case 1:")
    print(f"Input: {words1}")
    print(f"Output: {solution.palindromePairs(words1)}")
    # Expected: [[0,1],[1,0],[3,2],[2,4]]
    
    # Test Case 2: Empty string case
    words2 = ["bat", "tab", "cat"]
    print(f"\nTest Case 2:")
    print(f"Input: {words2}")
    print(f"Output: {solution.palindromePairs(words2)}")
    # Expected: [[0,1],[1,0]]
    
    # Test Case 3: Single character case
    words3 = ["a",""]
    print(f"\nTest Case 3:")
    print(f"Input: {words3}")
    print(f"Output: {solution.palindromePairs(words3)}")
    # Expected: [[0,1],[1,0]]