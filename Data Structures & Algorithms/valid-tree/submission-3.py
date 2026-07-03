class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False



        graph = defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)



        visited = set()
        def dfs(node):
            if node in visited:
                return 


            visited.add(node)

            for nei in graph[node]:
                dfs(nei)


        dfs(0)
        if len(visited) == n:
            return True
        else:
            return False

        

            
        