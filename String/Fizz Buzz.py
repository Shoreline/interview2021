# Just straightforward solution with a some consideration of scalability
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []

        # Dictionary to store all fizzbuzz mappings
        fizz_buzz_dict = {3: "Fizz", 5: "Buzz"}

        for i in range(1, n + 1):

            val = ""
            for num, text in fizz_buzz_dict.items():
                # If the num is divisible by key,
                # then add the corresponding string mapping to current num_ans_str
                if i % num == 0:
                    val += text  # "FizzBuzz" if i is divisible by 3 and 5.

            if not val:
                val = str(i)

            # Append the current answer str to the ans list
            ans.append(val)

        return ans

# Naive solution. Not very scalable.
# class Solution:
#     def fizzBuzz(self, n: int) -> List[str]:
#         res = []
#         i = 1
#         while i <= n:
#             if i % 3 == 0 and i % 5 == 0:
#                 res.append("FizzBuzz")
#             elif i % 3 == 0:
#                 res.append("Fizz")
#             elif i % 5 == 0:
#                 res.append("Buzz")
#             else:
#                 res.append(str(i))
#             i += 1
#         return res