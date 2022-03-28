# Need to ensure both ways of w_to_p and p_to_w have no conflict
# w_to_p[word] is simply pattern[i] (i is the index of word in s)
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(words) != len(pattern) or len(set(words)) != len(set(pattern)):
            return False

        w_to_p = {}
        for i, word in enumerate(words):
            if i >= len(pattern) or (word in w_to_p and w_to_p[word] != pattern[i]):
                return False
            else:
                w_to_p[word] = pattern[i]

        return True

