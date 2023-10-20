class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
        self.ref = 0
    
    def remove(self, word):
        cur = self
        cur.ref -= 1
        for w in word:
            cur = cur.children[w]
            cur.ref -= 1
    
    def addWord(self, word):
        cur = self
        cur.ref += 1
        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()
            cur = cur.children[w]
            cur.ref += 1
        cur.end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)
        
        visit, res = set(), []
        rows, cols = len(board), len(board[0])

        def dfs(r, c, node, word):
            if (r < 0 or c < 0 or r == rows or c == cols or board[r][c] not in node.children or (r, c) in visit or node.children[board[r][c]].ref < 1):
                return 
            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            
            if node.end:
                res.append(word)
                node.end = False
                root.remove(word)
            
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)

            visit.remove((r, c))

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "")
        return res