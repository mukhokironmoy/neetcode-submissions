class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows
        for i in range(9):
            check_rows = set()
            for j in range(9):
                if board[i][j] == ".":
                    continue
                elif board[i][j] in check_rows:
                    print("Row fail")
                    return False
                
                check_rows.add(board[i][j])

        # Check cols
        for i in range(9):
            check_cols = set()
            for j in range(9):
                if board[j][i] == ".":
                    continue
                elif board[j][i] in check_cols:
                    print("Col fail")
                    return False
                
                check_cols.add(board[j][i])

        
        # Create boxes
        boxes = []
        for i in range(3):
            boxes.append([])
            for j in range(3):
                boxes[i].append(set())

        
        # Check boxes
        for i in range(9):
            for j in range(9):
                box_row = i//3
                box_col = j//3

                if board[i][j] == ".":
                    continue
                elif board[i][j] in boxes[box_row][box_col]:
                    print("Box fail")
                    return False
                
                boxes[box_row][box_col].add(board[i][j])

        
        return True

        