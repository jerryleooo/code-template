class Solution:
    """
    @param: board: A list of lists of character
    @param: word: A string
    @return: A boolean
    """
    def exist(self, board, word):
        # write your code here

        def search(x, y, tree):
            
            if 'existed' in tree:
                return True
            
            dxs = [1, -1, 0, 0]
            dys = [0, 0, -1, 1]
            
            for dx, dy in zip(dxs, dys):
                new_x = x + dx
                new_y = y + dy
                if 0 <= new_x < len(board) and 0 <= new_y < len(board[0]) and board[new_x][new_y] in tree and (new_x, new_y) not in visited:
                    visited.add((new_x, new_y))
                    if search(new_x, new_y, tree[board[new_x][new_y]]):
                        return True
                    visited.remove((new_x, new_y))
                        
            return False

        trie = {}
        tree = trie
        visited = set()
        
        for c in word:
            if c not in tree:
                tree[c] = {}
            tree = tree[c]
        
        tree['existed'] = True
        
        for i, line in enumerate(board):
            for j, item in enumerate(line):
                if item == word[0]:
                    visited.add((i, j))
                    if search(i, j, trie[item]):
                        return True
                    visited.remove((i, j))
                        
        return False