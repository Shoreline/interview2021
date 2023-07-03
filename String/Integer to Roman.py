# Greedy algo, try divide the given number with Roman symbols (from big to small)
class Solution:
    def intToRoman(self, num: int) -> str:
        d = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V',
             4: 'IV', 1: 'I'}

        res = []

        for value in d:
            res.append((num // value) * d[value])
            num %= value

        return "".join(res)

# class Solution:
#     def intToRoman(self, num: int) -> str:
#         # ordered, so later we can use elements from 1000 to 1 in this sequence
#         digits = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"),
#                   (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"),
#                   (5, "V"), (4, "IV"), (1, "I")]

#         res = []
#         # Loop through each symbol.
#         for value, symbol in digits:
#             # We don't want to continue looping if we're done.
#             if num > 0:
#                 count, num = divmod(num, value)
#                 # Append "count" copies of "symbol" to res.
#                 res.append(symbol * count)
#         return "".join(res)