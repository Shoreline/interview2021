# Topological sort, similar to course scheduler

# ["wrt","wrf","er","ett","rftt"] -> "wertf"
#   - "rftt" does not mean f is before t! Only the words are sorted lexicographically. Characters in each word are not sorted!
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # <character, set<children_characters>> to represent a graph. Each character is a node.
        graph = collections.defaultdict(set)
        # in_degrees = Counter({c : 0 for word in words for c in word}) # only have keys for shown characters
        in_degrees = {c: 0 for word in words for c in word}

        for i in range(len(words) - 1):
            word1 = words[i]  # word1 is sorted to be ahead of word2
            word2 = words[i + 1]
            idx = 0
            for j in range(min(len(word1), len(word2))):
                c1, c2 = word1[j], word2[j]
                if c1 != c2:  # word1[j] is ahead of word2[j]
                    if c2 not in graph[c1]:  # found a new edge in graph, from c1 to c2
                        graph[c1].add(c2)
                        in_degrees[c2] += 1
                    break

                if len(word1) > len(word2) and j == len(word2) - 1:  # for corner cases like ["abc", "ab"]
                    return ""

        q = collections.deque()
        for c in in_degrees:
            if in_degrees[c] == 0:
                q.append(c)

        res = []
        while q:
            c = q.popleft()
            for child in graph[c]:
                in_degrees[child] -= 1
                if in_degrees[child] == 0:
                    q.append(child)

            res.append(c)

        if len(res) != len(in_degrees):  # if not all shown characters are in the result, means there is no solution
            return ""

        return ''.join(res)

# class Node(object):
#     def __init__(self):
#         self.IN = set()
#         self.OUT = set()

# class Solution(object):
#     def alienOrder(self, words):

#         # find out nodes
#         graph = {}
#         for word in words:
#             for letter in word:
#                 if letter not in graph:
#                     graph[letter] = Node()

#         # find out directed edges (from StefanPochmann)
#         for pair in zip(words, words[1:]):
#             for a, b in zip(*pair):
#                 if a != b:
#                     graph[a].OUT.add(b)
#                     graph[b].IN.add(a)
#                     break

#         # topo-sort
#         res = ""
#         while graph:
#             oldlen = len(graph)

#             for key in graph:
#                 if not graph[key].IN:   # to remove this
#                     for key2 in graph[key].OUT:
#                         graph[key2].IN.remove(key)
#                     del graph[key]
#                     res += key
#                     break

#             if oldlen == len(graph): # if shrinking stops, solution doesn't exist
#                 return ""
#             oldlen = len(graph)
#         return res