# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

# O(n). Keep checking one changeable candidate and ppl[i].
# We are told that there is at most ONE celebrity, making our lives much easier
#   - if knows(a, b) = True: a is not a celebrity;
#   - if knows(a, b) = False: b is not a celebrity
# Therefore, by running knows() once we can always eliminate one person
class Solution:
    def findCelebrity(self, n: int) -> int:
        candidate = 0
        for i in range(1, n):
            if knows(candidate, i):  # candidate is not the celebrity
                candidate = i  # try check i in future
            # else i is not the celebrity, so keep checking candidate

        # Verify if current candidate is the celebrity
        for i in range(n):
            if candidate != i and (knows(candidate, i) or not knows(i, candidate)):
                return -1

        return candidate

