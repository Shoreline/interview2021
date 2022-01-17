class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += carry
            carry = 0
            if digits[i] >= 10:
                digits[i] = digits[i] % 10
                carry = 1
        return digits if carry == 0 else [1] + digits
