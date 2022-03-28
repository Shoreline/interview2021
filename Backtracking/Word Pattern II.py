class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        return self.dfs(pattern, s, {})

    def dfs(self, pattern, s, p_to_w):
        if len(pattern) == 0 and len(s) > 0:
            return False
        if len(pattern) == len(s) == 0:
            return True

        # Optional optimization:
        # for end in range(1, len(s) + 1 - (len(pattern) - 1) ): # +2 because it is the "end of an end"
        # there is no sense to match a 5-character pattern to a str with 4 characters. Thus the first letter can map first k letters of the str. Here len(str) - k <= len(pattern) -1, thus k max is len(str) - len(pattern) + 1.

        for end in range(1, len(s) + 1):
            if pattern[0] not in p_to_w and s[:end] not in p_to_w.values():
                p_to_w[pattern[0]] = s[:end]
                if self.dfs(pattern[1:], s[end:], p_to_w):
                    return True
                del p_to_w[pattern[0]]
            elif pattern[0] in p_to_w and p_to_w[pattern[0]] == s[:end]:
                if self.dfs(pattern[1:], s[end:], p_to_w):
                    return True

        return False        