# Use an output stack to keep track of only non duplicate characters.
# T: O(N); S:O(N-D): D is the total length of all duplicates. Worst case O(N)
class Solution:
    def removeDuplicates(self, S: str) -> str:
        output = []
        for ch in S:
            if output and ch == output[-1]:  # found a duplicate
                output.pop()  # skip ch, and also pop stack[-1]
            else:
                output.append(ch)
        return ''.join(output)
