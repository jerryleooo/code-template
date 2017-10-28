import Queue

class Solution:
    """
    @param: board: board a 2D board containing 'X' and 'O'
    @return: nothing
    """
    def surroundedRegions(self, board):
        # write your code here

        if not board or not board[0]:
            return
        
        queue = Queue.Queue()
        row = len(board)
        col = len(board[0])
        
        for i in range(row):
            if board[i][0] == 'O':
                queue.put((i, 0))
            if board[i][col-1] == 'O':
                queue.put((i, col-1))
                
        for i in range(col):
            if board[0][i] == 'O':
                queue.put((0, i))
            if board[row-1][i] == 'O':
                queue.put((row-1, i))
                
        visited = set()
        directions = ((1, 0), (-1, 0), (0, -1), (0, 1))
                
        while not queue.empty():
            for i in range(queue.qsize()):
                x, y = queue.get()
                if (x, y) in visited:
                    continue
                visited.add((x, y))
                board[x][y] = '*'
                for dx, dy in directions:
                    if 0 <= x + dx < row and 0 <= y + dy < col and board[x+dx][y+dy] == 'O':
                        queue.put((x+dx, y+dy))
               
        mp = {'*': 'O', 'O': 'X', 'X': 'X'}
                        
        for i, line in enumerate(board):
            for j, node in enumerate(line):
                board[i][j] = mp[node]
                
                