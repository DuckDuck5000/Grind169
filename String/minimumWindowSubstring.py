class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Edge cases
        if not s or not t or len(s) < len(t):
            return ""
        
        # Initialize character frequency maps
        need = {}  # characters we need with their frequencies
        for c in t:
            need[c] = need.get(c, 0) + 1
        
        # Initialize variables
        window = {}  # current window character frequencies
        have = 0     # how many unique chars we have with correct frequencies
        required = len(need)  # how many unique chars we need
        
        # Initialize result tracking
        res = [float('inf'), 0, 0]  # [window length, left, right]
        
        # Sliding window
        left = 0
        for right in range(len(s)):
            # Add right character to window
            char = s[right]
            window[char] = window.get(char, 0) + 1
            
            # Check if this character meets its required frequency
            if char in need and window[char] == need[char]:
                have += 1
            
            # Try to minimize window while maintaining valid substring
            while have == required:
                # Update result if current window is smaller
                if (right - left + 1) < res[0]:
                    res = [right - left + 1, left, right + 1]
                
                # Remove left character from window
                left_char = s[left]
                window[left_char] -= 1
                
                # Check if removing left char breaks the required frequency
                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1
                
                left += 1
        
        return s[res[1]:res[2]] if res[0] != float('inf') else ""

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1: Regular case
    s1, t1 = "ADOBECODEBANC", "ABC"
    print(f"Test 1:")
    print(f"s = {s1}")
    print(f"t = {t1}")
    print(f"Result: {solution.minWindow(s1, t1)}")  # Expected: "BANC"
    
    # Test Case 2: When s and t are the same
    s2, t2 = "a", "a"
    print(f"\nTest 2:")
    print(f"s = {s2}")
    print(f"t = {t2}")
    print(f"Result: {solution.minWindow(s2, t2)}")  # Expected: "a"
    
    # Test Case 3: When no solution exists
    s3, t3 = "a", "b"
    print(f"\nTest 3:")
    print(f"s = {s3}")
    print(f"t = {t3}")
    print(f"Result: {solution.minWindow(s3, t3)}")  # Expected: ""