class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0] * numCourses

        queue = deque()

        for a,b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)
        order = []
        while queue:
            course = queue.popleft()

            order.append(course)

            for next_course in graph[course]:
                indegree[next_course] -= 1
                if indegree[next_course]== 0:
                    queue.append(next_course)
        
        if len(order) == numCourses:
            return order

        else :
            return []

                

        