# For words belonging to the same sequence:
#   each character in the word has the same relative offset comparing to the first_character of the word
# abc [0, 1, 2]
# bcd [0, 1, 2]
# acef [0, 2, 4, 5]
# xyz [0, 1, 2]
# az [0, 25]
# ba [0, 25]
# a [0]
# z [0]

# Saves the character offset sequence of each word: offset comparing to the first character.
# Note that the offset rotates back: the next char of z is a

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        offset_seq_dict = collections.defaultdict(list)

        for s in strings:
            first_c = s[0]

            key = []
            for c in s:
                offset = ord(c) - ord(first_c)
                if offset < 0:  # 'z' is 'a' - 1, and also 'a' + 25
                    offset += 26
                key.append(offset)

            offset_seq_dict[tuple(key)].append(s)  # need to distinguish "01" + "2" and "0" + "12"

        return offset_seq_dict.values()

class Solution2:
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
