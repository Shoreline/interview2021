# Just straightforward solution with a some consideration of scalability
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []

        # Dictionary to store all fizzbuzz mappings
        fizz_buzz_dict = {3 : "Fizz", 5 : "Buzz"}

        for num in range(1,n+1):

            val = ""

            for key in fizz_buzz_dict.keys():

                # If the num is divisible by key,
                # then add the corresponding string mapping to current num_ans_str
                if num % key == 0:
                    val += fizz_buzz_dict[key] # "FizzBuzz" if i is divisible by 3 and 5.

            if not val:
                val = str(num)

            # Append the current answer str to the ans list
            ans.append(val)

        return ans        