# PS:
# tickets[i] = [from_i, to_i]
# Reconstruct the itinerary in order and return it.
# All tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK"
# If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read
# as a single string.
#
# Example:
# Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
# Output: ["JFK","MUC","LHR","SFO","SJC"]

# DFS
# Use stack instead of queue for DFS -> starting airport of the next round has to be the destination airport from
# previous round
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        # Create a graph for each airport and keep list of airport reachable from it
        for src, dst in tickets:
            graph[src].append(dst)

        # Sort children list in descending order so that we can pop last element
        # instead of pop out first element which is costly operation
        for src in graph.keys():
            graph[src].sort(reverse=True)

        # Start with JFK as starting airport and keep adding the next child to traverse
        # for the last airport at the top of the stack. If we reach to an airport from where
        # we can't go further then add it to the result. This airport should be the last to go
        # since we can't go anywhere from here. That's why we return the reverse of the result
        # After this backtrack to the top airport in the stack and continue to traaverse it's children
        stack = ["JFK"]
        res = []

        while stack:
            elem = stack[-1]

            # Check if elem in graph as there may be a case when there is no out edge from an airport
            # In that case it won't be present as a key in graph
            if elem in graph and graph[elem]:  # graph[elem] is not empty
                stack.append(graph[elem].pop())
            else:
                # If there is no further children to traverse then add that airport to res
                # This airport should be the last to go since we can't anywhere from this
                # That's why we return the reverse of the result
                res.append(stack.pop())

        return res[::-1]
