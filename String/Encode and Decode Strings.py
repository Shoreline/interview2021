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
#         # Note, the is an additional ' | ' added to the end
#         return ''.join(s.replace('|', '||') + ' | ' for s in strs)
#
#     def decode(self, s: str) -> List[str]:
#         """Decodes a single string to a list of strings.
#         """
#         # To remove the additional ' | ' added to the end, we do [:-1]
#         return [t.replace('||', '|') for t in s.split(' | ')[:-1]]

# Chunked Transfer Encoding
# Send data in self-contained chunks, each of which is accompanied by its length or size.
class Codec2:
    def encode(self, strs):
        # Initialize an empty string to hold the encoded string.
        encoded_string = ''
        for s in strs:
            # Append the length, the delimiter, and the string itself.
            encoded_string += str(len(s)) + '/:' + s
        return encoded_string

    def decode(self, s):
        # Initialize a list to hold the decoded strings.
        decoded_strings = []
        i = 0
        while i < len(s):
            # Find the delimiter.
            delim = s.find('/:', i)
            # Get the length, which is before the delimiter.
            length = int(s[i:delim])
            # Get the string, which is of 'length' length after the delimiter.
            str_ = s[delim+2 : delim+2+length]
            # Add the string to the list.
            decoded_strings.append(str_)
            # Move the index to the start of the next length.
            i = delim + 2 + length
        return decoded_strings

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))