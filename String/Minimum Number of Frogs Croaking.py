# My own solution, passed :)
# T: O(n); S: O(1)
class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        d = {'c': 0, 'r': 1, 'o': 2, 'a': 3, 'k': 4}
        tracker = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}

        frogs = 0
        res = 0
        for c in croakOfFrogs:
            if d[c] == 0:
                tracker[d[c]] += 1
                frogs += 1
                res = max(res, frogs)
            elif d[c] > 0 and tracker[d[c] - 1] == 0:
                return -1
            else:
                tracker[d[c] - 1] -= 1
                tracker[d[c]] += 1

            if d[c] == 4:
                tracker[d[c]] -= 1
                frogs -= 1

        return res if frogs == 0 else -1