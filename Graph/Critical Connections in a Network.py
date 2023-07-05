# Note that node values are unique, and from 0 to n - 1
# A critical connection is a connection that, if removed, will make some servers unable to reach some other server.
#
# Tarjan's Bridge-Finding Algorithm TBFA is a bit like a combination of a depth-first search (DFS) approach with
# recursion and a union-find. IN TBFA, we do a recursive DFS on our graph and for each node we keep track of the
# earliest node that we can circle back around to reach. By doing this, we can identify whether a given edge is a
# bridge because the far node doesn't lead back to any other earlier node.

# To implement our TBFA, the first thing we have to do is to construct an edge map (edgeMap) from the connections
# list. Each key in our edge map should correspond to a specific node, and its value should be an array of each
# adjacent node to the key node.

# We'll also need separate arrays to store the discovery time (disc) and the lowest future node (low) for each node,
# as well as a time counter to use with disc.

# For our recursive DFS helper (dfs), each newly-visited node should set its initial value for both disc and low to
# the current value of time before time is incremented. (Note: If we start time at 1 instead of 0, we can use either
# disc or low as a visited array, rather than having to keep a separate array for the purpose. Any non-zero value in
# the chosen array will then represent a visited state for the given node.)

# Then we recursively call dfs on each of the unvisited adjacent nodes (next) of the current node (curr). If one of
# the possible next nodes is an earlier node (disc[next] < curr[low]), then we've found a loop and we should update
# the low value for the current node. As each layer of the recursive function backtracks, it will propagate this
# value of low back down the chain.

# If, after backtracking, the value of low[next] is still higher than disc[curr], then there is no looped connection,
# meaning that the edge between curr and next is a bridge, so we should add it to our answer array (ans).

# Once the dfs helper function has completed its traversal, we can return ans.
# example:
# for n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
# disc = [1, 2, 3, 4]
# low = [1, 1, 1, 4]
# Output: [[1,3]]
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        # construct the graph with given edges
        graph = defaultdict(list)
        for a, b in connections:
            graph[a].append(b)
            graph[b].append(a)

        time = [1]  # timer
        disc = [0] * n  # discovery time
        low = [0] * n   # lowest future node

        ans = []

        def dfs(curr: int, prev: int):
            disc[curr] = low[curr] = time[0]
            time[0] += 1
            # If one of the possible next nodes is an earlier node (disc[next] < low[curr]),
            # then we've found a loop and we should update the low value for the current node.
            for next in graph[curr]:
                if disc[next] == 0: # next is not yet visited
                    dfs(next, curr)
                    low[curr] = min(low[curr], low[next]) # propagate the value of low back from next to curr
                elif next != prev:  # next is already visited -> cycle
                    low[curr] = min(low[curr], disc[next]) # propagate the value of low back from next to curr

                # all nodes in a cycle will have the same low[i] value
                # so if low[next] > disc[curr], then curr,next is a critical edge
                if low[next] > disc[curr]:
                    ans.append([curr, next])

        dfs(0, -1)

        return ans
