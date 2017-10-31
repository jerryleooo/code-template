class Solution:
    """
    @param: board: A list of lists of character
    @param: words: A list of string
    @return: A list of string
    """
    def wordSearchII(self, board, words):
        # write your code here

        def build_trie(word):
            tree = trie
            for c in word:
                if c not in tree:
                    tree[c] = {}
                tree = tree[c]
            tree['existed'] = True

        def search(current, x, y, tree):
            if 'existed' in tree and current not in result:
                result.append(current)

            for dx, dy in directions:
                if 0 <= x + dx < len(board) and \
                    0 <= y + dy < len(board[0]) and \
                    board[x+dx][y+dy] in tree and \
                    (x+dx, y+dy) not in visited:

                    new_x, new_y, new_item = x + dx, y + dy, board[x+dx][y+dy]
                    visited.add((new_x, new_y))
                    search(current + new_item, new_x, new_y, tree[new_item])
                    visited.remove((new_x, new_y))            

        trie = {}
        result = []
        directions = ((0,1), (1,0), (0, -1), (-1, 0))
        visited = set()

        for word in words:
            build_trie(word)
            

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in trie:
                    visited.add((i, j))
                    search(board[i][j], i, j, trie[board[i][j]])
                    visited.remove((i, j))
                
        return result