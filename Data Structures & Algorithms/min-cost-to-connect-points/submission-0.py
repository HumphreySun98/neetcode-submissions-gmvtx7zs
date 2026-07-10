class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        parent = [i for i in range(n)]

        def find(i):
            if parent[i] == i:
                return i

            parent[i] = find(parent[i])
            return parent[i]

        def union(i,j):
            rootA = find(i)
            rootB = find(j)

            if rootA == rootB:
                return False

            parent[rootA] = rootB

            return True


        edge = []
        for i in range(n):
            for j in range(i+1,n):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1]-points[j][1])
                edge.append((dist,i,j))
        
        edge.sort()

        count = 0
        result = 0
        for dist,i,j in edge:
            if union(i,j):
                result += dist
                count += 1
                if count == n-1:
                    return result


        return result

        