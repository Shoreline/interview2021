# Key: convert s into a list first.
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s_list = list(s)
        i = 0
        while i < len(s_list):
            reverse_len = min(k, len(s_list) - i + 1)
            s_list[i:i + reverse_len] = reversed(s_list[i:i + reverse_len])
            i += 2 * k
        return "".join(s_list)
