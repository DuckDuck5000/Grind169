class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> node
        # Initialize dummy head and tail nodes
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node(self, node):
        """Add node right after head"""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        """Remove an existing node"""
        prev = node.prev
        new = node.next
        prev.next = new
        new.prev = prev

    def _move_to_front(self, node):
        """Move node to front (most recently used)"""
        self._remove_node(node)
        self._add_node(node)

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._move_to_front(node)  # Mark as most recently used
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update existing node
            node = self.cache[key]
            node.value = value
            self._move_to_front(node)
        else:
            # Add new node
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_node(new_node)
            
            # Remove least recently used if capacity exceeded
            if len(self.cache) > self.capacity:
                # Remove from both cache and linked list
                lru = self.tail.prev
                self._remove_node(lru)
                del self.cache[lru.key]

cache = LRUCache(2)  # Create cache with capacity 2
cache.put(1, 1)      # Cache is {1=1}
cache.put(2, 2)      # Cache is {1=1, 2=2}
cache.get(1)         # Returns 1
cache.put(3, 3)      # Removes key 2, cache is {1=1, 3=3}
cache.get(2)         # Returns -1 (not found)