# Remap each blacklisted item to a whitelisted item
class Solution:
    def __init__(self, N, blacklist):
        blacklist = set(blacklist)
        self.length = N - len(blacklist)
        self.remap = {}
        need_remap = []
        for x in blacklist:
            if x < self.length:
                need_remap.append(x)

        # map each blacklisted item in self.length to a whitelisted item outside of self.length
        j = 0
        for i in range(self.length, N):
            if i not in blacklist:
                self.remap[need_remap[j]] = i
                j += 1

    def pick(self):
        # idx = random.randrange(self.length)
        idx = random.randint(0, self.length - 1)
        return self.remap[idx] if idx in self.remap else idx

# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()