class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        h = Counter(secret)

        bulls = cows = 0
        for i, g in enumerate(guess):
            if g in h:  # if g in secret
                # corresponding characters match
                if g == secret[i]:
                    # update the bulls
                    bulls += 1
                    # update the cows
                    # Prioritize a bull over a cow
                    # if all g characters from secret were used up,
                    # we need to use the ones previous used as cows
                    if h[g] <= 0:
                        cows -= 1
                # corresponding characters don't match
                else:
                    # update the cows
                    if h[g] > 0:
                        cows += 1
                # ch character was used
                h[g] -= 1

        return str(bulls) + 'A' + str(cows) + 'B'

# One pass, even faster
# class Solution:
#     def getHint(self, secret: str, guess: str) -> str:
#         # map for both secret and guess
#         # For each character c in s, h[c] += 1
#         # For each character c in g, h[c] -= 1
#         h = defaultdict(int)
#         bulls = cows = 0

#         for i in range(len(secret)): # one pass to  check both secret and guess
#             s = secret[i]
#             g = guess[i]
#             if s == g:
#                 bulls += 1
#             else:
#                 if h[s] < 0:    # s showed up in guess before, and not picked as a cow
#                     cows += 1
#                 if h[g] > 0:    # g showed up in secret before, and not picked as a cow
#                     cows += 1

#                 h[s] += 1
#                 h[g] -= 1

#         return str(bulls) + 'A' + str(cows) + 'B'      