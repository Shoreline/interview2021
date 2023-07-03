# compare two strings with two pointers, one for each string
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = j = 0  # two pointers for the input word and abbr
        m, n = len(word), len(abbr)
        while i < m and j < n:
            if word[i] == abbr[j]:
                i += 1
                j += 1
            elif abbr[j].isnumeric() and abbr[j] != "0":
                # get the complete number in abbr
                k = j
                while k < n and abbr[k].isnumeric():
                    k += 1
                i += int(abbr[j:k])
                j = k
            else:  # either start with '0', or word[i] != abbr[j]
                return False
        return i == m and j == n
