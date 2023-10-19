class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root

        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()
            cur = cur.children[w]
        cur.end = True

    def search(self, word: str) -> bool:

        def dfs(node, j):
            cur = node
            for i in range(j, len(word)):
                w = word[i]
                if w == ".":
                    for child in cur.children.values():
                        if dfs(child, i + 1):
                            return True
                    return False
                else:  
                    if w not in cur.children:
                        return False
                    cur = cur.children[w]
            return cur.end

        return dfs(self.root, 0)

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)