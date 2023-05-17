class Solution:
    def toGoatLatin(self, S):
        vowel = set('aeiouAEIOU')
        def latin(w, i):
            if w[0] not in vowel:
                w = w[1:] + w[0]
            return w + 'ma' + 'a' * (i + 1)
        return ' '.join(latin(w, i) for i, w in enumerate(S.split()))