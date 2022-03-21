# Saves the character offset sequence of each word: offset comparing to the first character.
# Note that the offset rotates back: the next char of z is a

# class Solution:
#     def groupStrings(self, strings: List[str]) -> List[List[str]]:
#         offset_seq_dict = collections.defaultdict(list)

#         for s in strings:
#             first_c = s[0]

#             key = []
#             for c in s:
#                 offset = ord(c) - ord(first_c)
#                 if offset < 0:
#                     offset += 26
#                 key.append(str(offset))
#             offset_seq_dict["|".join(key)].append(s) # need to distinguish "01" + "2" and "0" + "12"

#         return offset_seq_dict.values()

# A tuple can be used as key of a map, but a list cannot
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        offset_seq_dict = collections.defaultdict(list)

        for s in strings:
            first_c = s[0]

            key = []
            for c in s:
                offset = ord(c) - ord(first_c)
                if offset < 0:
                    offset += 26
                key.append(offset)
            offset_seq_dict[tuple(key)].append(s)  # need to distinguish "01" + "2" and "0" + "12"

        return offset_seq_dict.values()
