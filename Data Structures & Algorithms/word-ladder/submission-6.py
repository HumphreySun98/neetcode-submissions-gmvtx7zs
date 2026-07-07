class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        wordList.append(beginWord)

        size = len(beginWord)
        patternmap = defaultdict(list)

        for word in wordList:
            for i in range(size):
                pattern = word[:i] + '#' + word[i+1:]
                patternmap[pattern].append(word)



        queue = deque([beginWord])
        visited = set([beginWord])
        
        count = 1

        while queue:
            queue_size = len(queue)
            for _ in range(queue_size):
                word = queue.popleft()
                for i in range(size):
                    pattern = word[:i] + '#' + word[i+1:]

                    for nei in patternmap[pattern]:
                        if nei == endWord:
                            return count +1

                        if nei not in visited:
                            visited.add(nei)
                            queue.append(nei)


            count += 1


        return 0


            