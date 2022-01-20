# Divide the input log into two lists, one for digit-log, one for letter-log
# Sort the letter-log with a custom comparator, then merge them together.
# (No need to sort digit-log, since we only need to keep their relative ordering)
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digits = []
        letters = []

        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)

        # when suffix is tie, sort by identifier
        # sort by the given tuple (a,b), returned by the lambda
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))

        result = letters + digits
        return result