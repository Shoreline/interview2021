class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cnt = Counter(ransomNote)
        for c in magazine:
            if c in cnt and cnt[c] > 0:
                cnt[c] -= 1

        return sum(cnt.values()) == 0
