# Sliding window without a fixed length
#   all characters in current window can be converted to the same char.
# The largest window we can find has this property: length = maxf + k
#   where maxf is the maximum character count within the window.
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        s = answerKey
        # current window: [i, j]
        maxf = i = 0
        count = collections.Counter() # char frequency in current window
        for j in range(len(s)):
            count[s[j]] += 1
            maxf = max(maxf, count[s[j]])

            # if window is too big to convert all chars within to be one char, shrink it.
            if j - i + 1 > maxf + k:
                count[s[i]] -= 1
                i += 1
        return len(s) - i