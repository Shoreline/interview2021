# Simple linear scanning of substring
# Time and space: O((N-L)*L), while L = 10 in this case, making them eventually O(N)
# substring building costs O(L)
# class Solution:
#     def findRepeatedDnaSequences(self, s: str) -> List[str]:
#         repeated, seen = set(), set()
#         for i in range(len(s)-9):
#             substring = s[i:i+10]
#             if substring in seen or substring in repeated:
#                 repeated.add(substring)

#             seen.add(substring)

#         return list(repeated)


# Rolling hash of substring
# Building hash value costs O(1), better than substring cost that takes O(L)
# Time and space: O(N - L), better than simple linear scanning
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        L, n = 10, len(s)
        if n <= L:
            return []

        # rolling hash parameters: base a
        a = 4
        aL = pow(a, L)  # a * a *... * a for L times

        # convert string to array of integers
        to_int = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        nums = [to_int.get(s[i]) for i in range(n)]

        h = 0
        seen, output = set(), set()
        # iterate over all sequences of length L
        for start in range(n - L + 1):

            if start == 0:
                # compute hash of the first sequence in O(L) time
                for i in range(L):
                    h = h * a + nums[i]
            else:
                # compute hash of the current sequence in O(1) time
                h = h * a - nums[start - 1] * aL + nums[start + L - 1]

            # update output and hashset of seen sequences
            if h in seen:
                output.add(s[start:start + L])
            seen.add(h)
        return output