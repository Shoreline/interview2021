# different cases
# 1. sign, and abs() both numerator and denominator after finding out the sign
# 2. whether need to handle fraction (does the result contain fractional numbers)
# 3. Use a map of <numerator, index> to determine if there is a repeat and where the repeat starts.
#    "index" is the index in the resulting string
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator % denominator == 0:
            return str(numerator // denominator)

        sign = '' if numerator * denominator >= 0 else '-'
        numerator, denominator = abs(numerator), abs(denominator)
        res = sign + str(numerator // denominator) + '.'

        numerator %= denominator  # both nu and de are >=0 now, so no need to think about % for negative number
        i, part = 0, ''
        m = {}  # <numerator, index> map. index is the index of numerator while inserting the "index" digit of part
        while numerator % denominator:
            if numerator in m:
                index = m[numerator]
                part = part[:index] + '(' + part[index:] + ')'
                break
            else:
                m[numerator] = i
                numerator *= 10
                part += str(numerator // denominator)
                numerator %= denominator
                i += 1

        return res + part
