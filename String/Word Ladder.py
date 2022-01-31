# !BFS
# Starting fromt he begin_word, try every possible 1-modification word, if any one of these variants are in WordList, then it is a node 1 distance away. Keep doing BFS until found the end_word or finished traversing the map
# We don't need clear separation between levels. Just keep searching until we find a fit.
#   So, we use tuple (word, distance) as queue element. (Instead of tracking distance of each level with a separate variable)
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)  # to track words haven't been visited
        queue = collections.deque([[beginWord, 1]])  # [word, distinace]

        while queue:
            word, distance = queue.popleft()
            if word == endWord:
                return distance

            # Add eligible 1-distance variants to the queue
            if not wordList:
                continue
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + c + word[i + 1:]
                    if next_word in wordList:
                        queue.append([next_word, distance + 1])
                        wordList.remove(next_word)  # don't forget this
        return 0