class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        i, j, n = 0, len(arr) - 1, len(arr)

        while i + 1 < n and arr[i] < arr[i + 1]:
            i += 1
        while j > 0 and arr[j - 1] > arr[j]:
            j -= 1

        return i == j and 0 < i < n - 1
