class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for i,j in sorted(tickets, reverse = True):
            graph[i].append(j)


        route = []

        def dfs(airport):
            while graph[airport]:
                next_airport = graph[airport].pop()

                dfs(next_airport)

            route.append(airport)

        dfs("JFK")
        return route[::-1]
         


        