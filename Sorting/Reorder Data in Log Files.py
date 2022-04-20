# Write a

# Let N be the number of logs in the list and M be the maximum length of a single log.
# T: O(M*N*logN); S: O(M*N)
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        def get_key(log):
            identifier, rest = log.split(" ", maxsplit=1)
            if rest[0].isalpha():
                return [0, rest, identifier]  # First sort by 0, then the text of rest, then identifier
            else:
                return [
                    1]  # For digit logs, just sort by 1 (after all letter logs), then keep their original sequence

        return sorted(logs, key=get_key)

# Divide the input log into two lists, one for digit-log, one for letter-log
# Sort the letter-log with a custom comparator, then merge them together.
# (No need to sort digit-log, since we only need to keep their relative ordering)
# class Solution:
#     def reorderLogFiles(self, logs: List[str]) -> List[str]:
#         digits = []
#         letters = []

#         for log in logs:
#             if log.split()[1].isdigit():
#                 digits.append(log)
#             else:
#                 letters.append(log)

#         #when suffix is tie, sort by identifier
#         # sort by the given tuple (a,b), returned by the lambda
#         letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))

#         result = letters + digits
#         return result        