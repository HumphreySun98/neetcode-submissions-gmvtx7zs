class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {}
        for word in words:
            for ch in word:
                adj[ch] = set()

        for i in range(len(words)-1):
            w1,w2 = words[i],words[i+1]
            min_len = min(len(w1),len(w2))
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""


            for j in range(min_len):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break


        indegree = {}
        for ch in adj:
            indegree[ch] = 0

        for ch in adj:
            for nei in adj[ch]:
                indegree[nei] += 1

        queue = deque()
        for ch in indegree:
            if indegree[ch] == 0:
                queue.append(ch)

        res = []
        while queue:
            char = queue.popleft()
            res.append(char)
            for nei in adj[char]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)


        if len(res) != len(indegree):
            return ""


        return "".join(res)



        