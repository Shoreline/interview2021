class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        char_count = Counter(s)
        odd_char = ''
        for c in char_count:
            if char_count[c] % 2 == 1:
                if odd_char != '':
                    return []
                else:
                    odd_char = c

        res = []
        tmp = [''] * len(s)
        tmp[len(s) // 2] = odd_char
        char_count[odd_char] -= 1

        def helper(pos, tmp):
            if pos == len(s) // 2:
                res.append(''.join(tmp[:]))
                return

            for c in char_count:
                if char_count[c] > 0:
                    tmp[pos] = c
                    tmp[len(s) - 1 - pos] = c
                    char_count[c] -= 2
                    helper(pos + 1, tmp)
                    char_count[c] += 2

        helper(0, tmp)

        return res
