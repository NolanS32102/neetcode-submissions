class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row in board:
            s = set()
            for element in row:
                if element in s and element != ".":
                    return False
                elif element != ".":
                    s.add(element)

        for col in range(len(board[0])):
            s = set()
            for row in range(len(board)):
                if board[row][col] in s and board[row][col] != ".":
                    return False
                elif board[row][col] != ".":
                    s.add(board[row][col])
        
        for square in range(len(board)):
            s = set()
            for i in range(3):
                for j in range(3):
                    row = (square // 3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] in s and board[row][col] != ".":
                        return False
                    elif board[row][col] != ".":
                        s.add(board[row][col])

        return True

    # Check the rows for dupes O(n^2)
    # Check the cols for dupes O(n^2)
    # Check the each box for dupes
