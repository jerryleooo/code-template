class Solution:
    """
    @param: n: The number of queens
    @return: All distinct solutions
    """
    def solveNQueens(self, n):
        # write your code here

        def search(cols):
            if len(cols) == n:
                result.append(draw_chess_board(cols))
                return

            for i in range(n):
                if not is_valid(cols, i):
                    continue
                search(cols + [i])
                
        def is_valid(cols, col):
            # cols[1]=4 表示第一行的皇后是在第四列上
            # row 代表正在处理的这行，那么 (row, col) 是下一个可能的 Q 坐标
            # 对角线是 X - Y == 0
            # 斜对角线是 X + Y == 固定值

            row = len(cols)
            for i in range(row):
                if cols[i] == col: # 同一列上已经有皇后 
                    return False
                if i + cols[i] == row + col: # 在同斜对角线上
                    return False
                if i - cols[i] == row - col: # 在同一对角线上
                    return False
            return True
                    
        def draw_chess_board(cols):
            chessboard = []
            for i in range(len(cols)):
                line = []
                for j in range(len(cols)):
                    line.append('Q' if cols[i] == j else '.')
                chessboard.append("".join(line))
            return chessboard

        result = []
        if n <= 0:
            return result
            
        search([])
        return result