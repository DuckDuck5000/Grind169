from collections import defaultdict

class TimeMap:
    def __init__(self):
        # Initialize with defaultdict of lists to store {key: [(timestamp, value),...]}
        self.store = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        # Add new timestamp-value pair to the list for this key
        self.store[key].append((timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        # If key doesn't exist, return empty string
        if key not in self.store:
            return ""
        
        values = self.store[key]
        
        # Binary search to find the largest timestamp <= target
        left, right = 0, len(values) - 1
        
        # Handle edge cases
        if values[left][0] > timestamp:
            return ""
        if values[right][0] <= timestamp:
            return values[right][1]
            
        # Binary search
        while left <= right:
            mid = (left + right) // 2
            if values[mid][0] <= timestamp:
                if values[mid + 1][0] > timestamp:
                    return values[mid][1]
                left = mid + 1
            else:
                right = mid - 1
                
        return ""

# Test cases
if __name__ == "__main__":
    timeMap = TimeMap()
    
    # Test case 1: Basic functionality
    print("Test Case 1:")
    timeMap.set("foo", "bar", 1)
    result1 = timeMap.get("foo", 1)
    assert result1 == "bar", f"Expected 'bar', but got '{result1}'"
    result2 = timeMap.get("foo", 3)
    assert result2 == "bar", f"Expected 'bar', but got '{result2}'"
    
    # Test case 2: Multiple values for same key
    print("Test Case 2:")
    timeMap.set("foo", "bar2", 4)
    result3 = timeMap.get("foo", 4)
    assert result3 == "bar2", f"Expected 'bar2', but got '{result3}'"
    result4 = timeMap.get("foo", 5)
    assert result4 == "bar2", f"Expected 'bar2', but got '{result4}'"
    
    # Test case 3: Non-existent key
    print("Test Case 3:")
    result5 = timeMap.get("nonexistent", 1)
    assert result5 == "", f"Expected '', but got '{result5}'"
    
    # Test case 4: Timestamp before first entry
    print("Test Case 4:")
    result6 = timeMap.get("foo", 0)
    assert result6 == "", f"Expected '', but got '{result6}'"
    
    print("All test cases passed!")