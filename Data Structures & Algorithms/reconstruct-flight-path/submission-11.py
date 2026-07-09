class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for i,j in sorted(tickets, reverse = True):
            graph[i].append(j)


        stack = ["JFK"]
        route = []
         

        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop())

            route.append(stack.pop())

        return route[::-1]


        