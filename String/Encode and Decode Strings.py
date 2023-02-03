# Encoding: just concatenate input array with ' | '
#   Note that ' | ' has two spaces before and after
#   Replace existing '|' with '||';#
# Deconding: split the given string by ' | '
class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        haha = [s.replace('|', '||') for s in strs]
        return ' | '.join(haha)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        haha = s.split(' | ')
        return [ha.replace('||', '|') for ha in haha]
# class Codec:
#     def encode(self, strs: List[str]) -> str:
#         """Encodes a list of strings to a single string.
#         """
#         return ''.join(s.replace('|', '||') + ' | ' for s in strs)
#
#     def decode(self, s: str) -> List[str]:
#         """Decodes a single string to a list of strings.
#         """
#         return [t.replace('||', '|') for t in s.split(' | ')[:-1]]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))