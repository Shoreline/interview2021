# To do it without build-in function, write 3 functions:
# step 1. reverse the whole string
# step 2. reverse each word
# step 3. clean up spaces
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))

# class Solution:
#     def reverseWords(self, s: str) -> str:
#         return " ".join(s.split()[::-1])
