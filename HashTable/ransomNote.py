class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        
        rans = Counter(ransomNote)
        mag = Counter(magazine)
        
        
        for key, value in rans.items():
            
            if key not in mag or not (key in mag and mag[key] >= value):
                return False
        return True 