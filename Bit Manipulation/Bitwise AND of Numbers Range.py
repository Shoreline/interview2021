# AND: if there is one zero in a sequence of bits, then the AND result will be 0.
#
# Transform this problem into finding the common prefix of the two given numbers
# Obviously, as long as left != right, there are > 1 different numbers (diff by 1)
#   -> The last bit has at least one 0
#   -> After AND, the last bit will be 0
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        i = 0
        while left != right:  # when left and right still haven't got the same prefix
            left >>= 1
            right >>= 1
            i += 1
        return right << i
