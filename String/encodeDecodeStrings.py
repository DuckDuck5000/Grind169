class Solution:
    def encode(self, strs: list[str]) -> str:
        """Encodes a list of strings to a single string."""
        # Use length + delimiter + string pattern
        # Format: [length]#[string] for each string
        return ''.join(f'{len(s)}#{s}' for s in strs)
    
    def decode(self, s: str) -> list[str]:
        """Decodes a single string to a list of strings."""
        result = []
        i = 0
        
        while i < len(s):
            # Find the delimiter '#'
            j = i
            while s[j] != '#':
                j += 1
            
            # Get length of the next string
            length = int(s[i:j])
            
            # Extract the string using length
            string = s[j + 1:j + 1 + length]
            result.append(string)
            
            # Move pointer to start of next length
            i = j + 1 + length
        
        return result

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1: Regular strings
    input1 = ["Hello", "World"]
    print(f"Test 1 Input: {input1}")
    encoded = solution.encode(input1)
    print(f"Encoded: {encoded}")
    decoded = solution.decode(encoded)
    print(f"Decoded: {decoded}")
    print(f"Matches original: {input1 == decoded}\n")
    
    # Test Case 2: Empty strings and special characters
    input2 = ["", "abc", "###"]
    print(f"Test 2 Input: {input2}")
    encoded = solution.encode(input2)
    print(f"Encoded: {encoded}")
    decoded = solution.decode(encoded)
    print(f"Decoded: {decoded}")
    print(f"Matches original: {input2 == decoded}")