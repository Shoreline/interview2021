# Given an integer x, return true if x is a palindrome, and false otherwise.

# The most straightforward, compare head and tail digits for 101211: it becomes 121 in the 2nd round. But now div is
# 1000, so 121/1000 = 0 still gives the correct number of the 2nd left-most digit. And since 121/1000 = 0 != 121%10,
# so we can get the right answer.
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        div = 1
        while x // div > 9:
            div *= 10

        while x > 0:
            if x // div != x % 10:
                return False

            # We need to shrink x by two digits
            # Both its head and tail digits need to be removed
            x = (x % div) // 10

            # easy to just //10
            div = div // 100

        return True

# Solution 2
# get the reversed number and compare it with the given input
#   - need to be careful for integer overflow
# public class Solution {
#     public bool IsPalindrome(int x) {
#         // Special cases:
#         // As discussed above, when x < 0, x is not a palindrome.
#         // Also if the last digit of the number is 0, in order to be a palindrome,
#         // the first digit of the number also needs to be 0.
#         // Only 0 satisfy this property.
#         if(x < 0 || (x % 10 == 0 && x != 0)) {
#             return false;
#         }

#         int revertedNumber = 0;
#         while(x > revertedNumber) {
#             revertedNumber = revertedNumber * 10 + x % 10;
#             x /= 10;
#         }

#         // When the length is an odd number, we can get rid of the middle digit by revertedNumber/10
#         // For example when the input is 12321, at the end of the while loop we get x = 12, revertedNumber = 123,
#         // since the middle digit doesn't matter in palidrome(it will always equal to itself), we can simply get rid of it.
#         return x == revertedNumber || x == revertedNumber/10;
#     }
# }