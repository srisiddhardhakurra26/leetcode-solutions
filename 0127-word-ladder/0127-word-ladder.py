class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q, res = deque(), 0
        adjList = defaultdict(list)
        wordList.append(beginWord)
        visit = set()
        for word in wordList:
            pattern = ""
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i + 1:]
                adjList[pattern].append(word)
        q.append(beginWord)
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res + 1
                pattern = ""
                for i in range(len(word)):
                    pattern = word[:i] + '*' + word[i + 1:]
                    if pattern in visit:
                        continue
                    for w in adjList[pattern]:
                        q.append(w)
                        visit.add(pattern)
            res += 1
        return 0