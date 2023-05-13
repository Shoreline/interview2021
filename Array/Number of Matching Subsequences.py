# Since length of string s is big, let's think a way to iterate chracters in string s once.
# We can group words into buckets by their starting character.
# Then we iterate characters c in string s, we process words in bucket[c] by trimming their starting character:
#   If the word after trimming is empty -> then it's a subsequence of string s -> ans += 1.
#   Else group the word after trimming into corresponding buckets by its starting character.
#
# https://leetcode.com/problems/number-of-matching-subsequences/solutions/1290406/c-java-python-process-by-bucket-picture-explain-o-n-s/?orderBy=most_votes

class Node:
    def __init__(self, word):
        self.word = word
        self.index = 0

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        buckets = defaultdict(list)
        for word in words:
            startingChar = word[0]
            buckets[startingChar].append(Node(word))

        ans = 0
        for c in s:
            currBucket = buckets[c]
            buckets[c] = []
            for node in currBucket:
                node.index += 1  # Point to next character of node.word
                if node.index == len(node.word):
                    ans += 1
                else:
                    startingChar = node.word[node.index]
                    buckets[startingChar].append(node)
        return ans