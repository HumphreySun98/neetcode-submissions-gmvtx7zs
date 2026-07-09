class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for i, j in sorted(tickets):
            graph[i].append(j)


        n = len(tickets)

        path = ["JFK"]


        def bt(airport):
            if len(path) == n+1:
                return True

            destination = graph[airport]
            for i in range(len(destination)):
                dst = destination[i]
                path.append(dst)
                destination.pop(i)

                if bt(dst):
                    return True

                path.pop()

                destination.insert(i,dst)

            return False

        
        bt("JFK")
        return path


                    

        