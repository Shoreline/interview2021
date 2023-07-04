# 1) first half of a row is always the same as previous row
# 2) second half is the NOT of first half
# 0
# 01
# 0110
# 01101001
# ....
class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        # Think of the base case, already given here though
        if N == 1 and K == 1:
            return 0

        # We need to do some observation here:
        # 1 - Calculate the length of every row which is as below
        # 2 ^ (N-1) is the total length. So mid is half of it
        mid = (2 ** (N - 1)) // 2

        # If the K lies in the first half, it is actually same as prev row
        if K <= mid:
            return int(self.kthGrammar(N - 1, K))
        else:
            # Else it subtract the first half and then it is same as
            # complement of the prev row
            return int(not self.kthGrammar(N - 1, K - mid))