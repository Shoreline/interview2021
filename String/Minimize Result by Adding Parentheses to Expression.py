# PS: You are given a 0-indexed string expression of the form "<num1>+<num2>" where <num1> and <num2> represent
# positive integers.

# Break the expression into four numbers like expression = first + second. Then break both left and right into two
# numbers: first = num1, num2 and second = num 3 and num 4.

# Calculate the result with of these four numbers with the equation: num1(num2 + num3)num4 , and keep track of the
# minimal result. Once a minimal found, update the result

# Note that num2 and num3 must be valid numbers! While num1 and num4 can be empty.
class Solution:
    def minimizeResult(self, expression: str) -> str:
        first, second = expression.split('+')
        score = float('inf')
        res = ''
        for i in range(len(first)):
            # split 'first' into two numbers
            num_1 = int(first[:i]) if i > 0 else 1
            num_2 = int(first[i:])

            for j in range(1, len(second) + 1):
                # split 'second' into two numbers
                num_3 = int(second[:j])
                num_4 = int(second[j:]) if j < len(second) else 1
                cur_score = num_1 * (num_2 + num_3) * num_4
                if cur_score < score:
                    # Wrong!
                    # num_1 and num_4 may not be converted from strings
                    # res = str(num_1) + '(' + str(num_2) + '+' + str(num_3) + ')' + str(num_4)

                    res = first[:i] + '(' + first[i:] + '+' + second[:j] + ')' + second[j:]

                    score = cur_score

        return res
