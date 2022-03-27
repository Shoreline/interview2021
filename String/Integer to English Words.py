class Solution:
    def numberToWords(self, num: int) -> str:
        less_than_20 = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven",
                        "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

        def get_words(n) -> list[str]:
            if n == 0:
                return []
            if n < 20:
                return [less_than_20[n - 1]]
            if n < 100:
                return [tens[n // 10 - 2]] + get_words(n % 10)  # n//10 - 2: -2 since the list tens starting from Twenty
            if n < 1000:
                return [less_than_20[n // 100 - 1]] + ['Hundred'] + get_words(n % 100)

            for i, w in enumerate(['Thousand', 'Million', 'Billion']):
                if n < 1000 ** (i + 2):
                    return get_words(n // 1000 ** (i + 1)) + [w] + get_words(n % 1000 ** (i + 1))

        res = get_words(num)
        return ' '.join(res) if res else "Zero"