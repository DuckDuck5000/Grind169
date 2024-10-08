class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        

        
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                
                if board[i][j] == word[0] and self.wordSearch(board, i, j, 0, word):
                    return True
        return False
    
    def wordSearch(self, board, i, j, count, word):
        
        if count == len(word):
            return True
        
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[i])or board[i][j] !=word[count]:
            return False
        
        temp = board[i][j]
        board[i][j] = ''
        
        found =  (self.wordSearch(board, i+1, j,count + 1, word) or self.wordSearch(board, i-1, j, count +1, word) or self.wordSearch(board, i, j-1, count + 1, word) or self.wordSearch(board, i, j+1, count + 1, word))
        board[i][j] = temp
        
        return found