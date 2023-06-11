# Build a value-indices map of dict<value, list<index>>.
# For a target, randomly pick one of the index in the list.
class Solution:
    def __init__(self, nums: List[int]):
        self.index_dict = defaultdict(list)
        for i in range(len(nums)):
            self.index_dict[nums[i]].append(i)

    def pick(self, target: int) -> int:
        return random.choice(self.index_dict[target])

# Reservoir Sampling solution
# pick: O(n) -> tle for new tests
# class Solution:

#     def __init__(self, nums: List[int]):
#         self.nums = nums

# 	# Time complexity: O(n), where "n" is the length of self.nums
#     def pick(self, target: int) -> int:
#         # how many samples with value "target" we have seen so far
#         n_samples = 0

# 		# result, selected index
#         reservoir = 0

# 		# iterate over all the values in self.nums
#         for index, value in enumerate(self.nums):
#             if value == target:
# 				# target value is found, increment the number of samples with value "target" found so far
#                 n_samples += 1

# 				# if it is the first sample found, just keep it index
#                 if n_samples == 1:
#                     reservoir = index
#                 else:
# 					# if there are more than 1 sample, randomly select any of them
#                     nth_sample = randint(1, n_samples)

#                     # At the chance of 1/n_samples
# 					# -> if the selected sample matches the first sample selected initially, then replace it
#                     if nth_sample == 1:
#                         reservoir = index
#         return reservoir


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)