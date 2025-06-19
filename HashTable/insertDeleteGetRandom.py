"""
Insert Delete GetRandom O(1)

Problem Description:
------------------
Implement the RandomizedSet class:
- RandomizedSet(): Initializes the empty set
- bool insert(int val): Inserts val if not present, returns true if val was not present
- bool remove(int val): Removes val if present, returns true if val was present
- int getRandom(): Returns random element from current set of elements
                  (Each element must have equal probability of being returned)

All operations should have average time complexity O(1)

Examples:
--------
Input:
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output:
[null, true, false, true, 2, true, false, 2]
"""

import random

class RandomizedSet:
    def __init__(self):
        # Dictionary to store value -> index mapping
        self.val_to_idx = {}
        # List to store values (for getRandom)
        self.values = []

    def insert(self, val: int) -> bool:
        # If value already exists
        if val in self.val_to_idx:
            return False
        
        # Add value to list and store its index
        self.values.append(val)
        self.val_to_idx[val] = len(self.values) - 1
        return True

    def remove(self, val: int) -> bool:
        # If value doesn't exist
        if val not in self.val_to_idx:
            return False
        
        # Get index of value to remove
        idx = self.val_to_idx[val]
        last_val = self.values[-1]
        
        # Move last element to idx position
        self.values[idx] = last_val
        self.val_to_idx[last_val] = idx
        
        # Remove the last element
        self.values.pop()
        del self.val_to_idx[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.values)

def run_tests():
    """Test cases with assertions"""
    # Test case 1: Basic operations
    rs = RandomizedSet()
    assert rs.insert(1) == True, "Failed to insert 1"
    assert rs.remove(2) == False, "Removing non-existent value should return False"
    assert rs.insert(2) == True, "Failed to insert 2"
    # Get random should return either 1 or 2
    random_val = rs.getRandom()
    assert random_val in [1, 2], f"getRandom returned {random_val}, expected 1 or 2"
    assert rs.remove(1) == True, "Failed to remove 1"
    assert rs.insert(2) == False, "Inserting duplicate should return False"
    
    # Test case 2: Multiple operations
    rs2 = RandomizedSet()
    assert rs2.insert(0) == True
    assert rs2.insert(1) == True
    assert rs2.remove(0) == True
    assert rs2.insert(2) == True
    assert rs2.remove(1) == True
    assert rs2.getRandom() == 2, "Only 2 should be in the set"
    
    print("All test cases passed!")

if __name__ == "__main__":
    run_tests()