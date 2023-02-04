# Saves the character offset sequence of each word: offset comparing to the first character.
# Note that the offset rotates back: the next char of z is a

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:

        def encode(s):
            res = []
            for i in range(1, len(s)):
                val = (26 + ord(s[0]) - ord(s[i])) % 26  # to deal with "rotation" issue!
                res.append(str(val))
            return ''.join(res)

        str_map = collections.defaultdict(list)
        for s in strings:
            str_map[encode(s)].append(s)
        return list(str_map.values())
