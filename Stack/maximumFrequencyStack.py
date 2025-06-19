class FreqStack:
    """
    LeetCode 895: Maximum Frequency Stack
    
    Design a stack-like data structure that pushes and pops the most frequent element.
    If there is a tie for most frequent element, the element closest to the top of the stack is removed.
    """
    
    def __init__(self):
        self.freq = {}  # Map element to its frequency
        self.group = {}  # Map frequency to stack of elements
        self.maxfreq = 0  # Current maximum frequency
        
    def push(self, val: int) -> None:
        # Update frequency of the element
        freq = self.freq.get(val, 0) + 1
        self.freq[val] = freq
        
        # Update maximum frequency
        self.maxfreq = max(self.maxfreq, freq)
        
        # Add element to its frequency group
        if freq not in self.group:
            self.group[freq] = []
        self.group[freq].append(val)
        
    def pop(self) -> int:
        # Get the most frequent element
        val = self.group[self.maxfreq].pop()
        
        # Update frequency
        self.freq[val] -= 1
        
        # If no more elements with current maxfreq
        if not self.group[self.maxfreq]:
            self.maxfreq -= 1
            
        return val