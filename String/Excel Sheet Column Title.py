# /*
#  * why n-- in each while loop?
#  *
#  * Because the smallest digit in this special 26-进制 mechanism is 1 instead of 0.
#  */
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []

        while columnNumber > 0:
            columnNumber -= 1 # since sheet column title is 1-based, not 0-based
            c = chr(ord("A") + columnNumber % 26)
            res.append(c)
            columnNumber //= 26

        return "".join(res[::-1])