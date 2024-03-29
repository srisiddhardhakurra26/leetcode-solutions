class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root

        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()
            cur = cur.children[w]
        cur.end = True

    def search(self, word: str) -> bool:
        cur = self.root

        for w in word:
            if w not in cur.children:
                return False
            cur = cur.children[w] 
        return cur.end
        
    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for p in prefix:
            if p not in cur.children:
                return False
            cur = cur.children[p]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)