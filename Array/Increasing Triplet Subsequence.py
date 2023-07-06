class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first_num = float("inf")
        second_num = float("inf")
        for n in nums:
            if n <= first_num:
                first_num = n
            elif n <= second_num: # here first_num exists, and first_num < n <= second_num
                second_num = n
            else:   # here first_num and second_num exist, and second_num < n
                return True
        return False