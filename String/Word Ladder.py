# !BFS
#
# Starting from the begin_word, try every possible 1-modification word, if any one of these variants are in WordList,
# then it is a node which is 1 distance away. Keep doing BFS until found the end_word or finished traversing the map
# We don't need a clear separation between levels. Just keep searching until we find a fit. So, we use tuple (word,
# distance) as queue element. (Instead of tracking distance of each level with a separate variable)

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)

        cur_lvl = [beginWord]
        lvl = 1
        while cur_lvl:
            next_lvl = []
            for word in cur_lvl:
                if word == endWord:
                    return lvl
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = word[:i] + c + word[i + 1:]
                        if new_word in word_set:
                            next_lvl.append(new_word)
                            # Instead of using another "seen" set, just remove it from word_set
                            word_set.remove(new_word)
            cur_lvl = next_lvl
            lvl += 1

        return 0

# class Solution:
#     def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
#         word_set = set(wordList)  # to track words haven't been visited
#         queue = collections.deque([[beginWord, 1]])  # [word, distance]
#
#         while queue:
#             word, distance = queue.popleft()
#             if word == endWord:
#                 return distance
#
#             # Add eligible 1-distance variants to the queue
#             if not word_set:
#                 continue
#             for i in range(len(word)):
#                 for c in 'abcdefghijklmnopqrstuvwxyz':
#                     next_word = word[:i] + c + word[i + 1:]
#                     if next_word in word_set:
#                         queue.append([next_word, distance + 1])
# Instead of using another "seen" set, just remove it from word_set
#                         word_set.remove(next_word)
#         return 0