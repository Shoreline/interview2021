# Time: O(N)
# Whether there is an answer or not all depends on the most frequent character
#   if the max_freq is too high, then no answer.
class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        char_freqs = Counter(s)  # character frequency
        max_count, max_c = 0, ''
        for char, count in char_freqs.items():
            if count > max_count:
                max_count = count
                max_c = char
        # if max_count > len(s) // 2 + len(s) % 2: # same
        if max_count > (n + 1) // 2:
            return ""

        # Prepare to place characters to the res[]
        res = [None] * n
        i = 0

        # 1) Place the most frequent max_c
        while char_freqs[max_c] != 0:
            res[i] = max_c
            i += 2
            char_freqs[max_c] -= 1

        # 2) Place rest of the letters in any order
        for char, count in char_freqs.items():
            while count > 0:
                # Reset index
                if i >= n:  # Always iterate res just twice. So only need one reset
                    i = 1
                res[i] = char
                i += 2
                count -= 1

        return ''.join(res)
