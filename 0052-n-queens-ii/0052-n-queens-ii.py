class Solution:
    def totalNQueens(self, n: int) -> int:
        pDiagonal, nDiagonal, col = set(), set(), set()
        res = 0
        board = [["."] * n for i in range(n)]

        def backtrack(r):
            nonlocal res
            if r == n:
                res += 1
                return

            for c in range(n):
                if c in col or (r + c) in pDiagonal or (r - c) in nDiagonal:
                    continue
                
                col.add(c)
                pDiagonal.add(r + c)
                nDiagonal.add(r - c)
                board[r][c] = "Q"

                backtrack(r + 1)

                col.remove(c)
                pDiagonal.remove(r + c)
                nDiagonal.remove(r - c)
                board[r][c] = "."
        
        backtrack(0)
        return res