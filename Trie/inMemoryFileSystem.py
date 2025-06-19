"""
Design In-Memory File System

Problem Description:
------------------
Design a data structure that simulates an in-memory file system with directories and files.
Implement the FileSystem class:
- FileSystem() Initializes the object of the system
- List<String> ls(String path) Returns sorted list of directory contents
- void mkdir(String path) Creates a new directory 
- void addContentToFile(String filePath, String content) Adds content to a file
- String readContentFromFile(String filePath) Returns the content of a file

Examples:
--------
Input: 
["FileSystem", "ls", "mkdir", "addContentToFile", "ls", "readContentFromFile"]
[[], ["/"], ["/a/b/c"], ["/a/b/c/d", "hello"], ["/"], ["/a/b/c/d"]]
Output:
[null, [], null, null, ["a"], "hello"]

Approach:
--------
1. Use Trie-like structure where each node represents file/directory
2. Each node tracks:
   - name (file/directory name)
   - isFile (boolean)
   - content (for files)
   - children (map of child directories/files)
3. Time Complexity: 
   - ls: O(m + nlogn) where m is path length, n is number of children
   - mkdir: O(m) where m is path length
   - addContent/readContent: O(m) where m is path length
4. Space Complexity: O(M) where M is total length of all paths/contents
"""

class FileNode:
    def __init__(self):
        self.children = {}  # Map of child nodes
        self.content = ""   # File content
        self.isFile = False # Whether node is a file

class FileSystem:
    def __init__(self):
        self.root = FileNode()

    def ls(self, path: str) -> list[str]:
        # Navigate to target node
        node = self.root
        files = []
        
        if path != "/":
            # Split path and traverse
            parts = path.split("/")[1:]
            for part in parts:
                if part not in node.children:
                    return []
                node = node.children[part]
            
            # If it's a file, return just the filename
            if node.isFile:
                return [parts[-1]]
        
        # Return sorted list of children
        return sorted(node.children.keys())

    def mkdir(self, path: str) -> None:
        node = self.root
        
        # Split path and create directories
        parts = path.split("/")[1:]
        for part in parts:
            if part not in node.children:
                node.children[part] = FileNode()
            node = node.children[part]

    def addContentToFile(self, filePath: str, content: str) -> None:
        node = self.root
        
        # Navigate to file location
        parts = filePath.split("/")[1:]
        for i in range(len(parts)):
            part = parts[i]
            if part not in node.children:
                node.children[part] = FileNode()
            node = node.children[part]
            
        # Add content to file
        node.isFile = True
        node.content += content

    def readContentFromFile(self, filePath: str) -> str:
        node = self.root
        
        # Navigate to file
        for part in filePath.split("/")[1:]:
            node = node.children[part]
        
        return node.content

def run_tests():
    """Test cases with assertions"""
    fs = FileSystem()
    
    # Test case 1: Basic operations
    assert fs.ls("/") == [], "Test case 1.1 failed"
    fs.mkdir("/a/b/c")
    fs.addContentToFile("/a/b/c/d", "hello")
    assert sorted(fs.ls("/")) == ["a"], "Test case 1.2 failed"
    assert fs.readContentFromFile("/a/b/c/d") == "hello", "Test case 1.3 failed"
    
    # Test case 2: File operations
    fs.addContentToFile("/a/b/c/d", " world")
    assert fs.readContentFromFile("/a/b/c/d") == "hello world", "Test case 2 failed"
    
    # Test case 3: Directory listing
    fs.mkdir("/a/b/e")
    assert sorted(fs.ls("/a/b")) == ["c", "e"], "Test case 3 failed"
    
    print("All test cases passed!")

if __name__ == "__main__":
    run_tests()