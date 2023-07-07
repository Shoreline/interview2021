class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        i, j, n = 0, len(arr) - 1, len(arr)

        # Move from left and stop at somewhere
        while i + 1 < n and arr[i] < arr[i + 1]:
            i += 1

        # Move from right and stop at somewhere
        while j > 0 and arr[j - 1] > arr[j]:
            j -= 1

        # see if meeting at one point in the middle
        return i == j and 0 < i < n - 1