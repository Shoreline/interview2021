class Solution:
    def __init__(self, nums: List[int]):
        self.index_dict = defaultdict(list)
        for i, num in enumerate(nums):
            self.index_dict[num].append(i)

    def pick(self, target: int) -> int:
        return random.choice(self.index_dict[target])


# Reservoir Sampling solution (TLE)
# pick: O(n) -> tle for new tests
class Solution2:

    def __init__(self, nums: List[int]):
        self.nums = nums

    # Time complexity: O(n), where "n" is the length of self.nums
    def pick(self, target: int) -> int:
        # how many samples with value "target" we have seen so far
        num_found_samples = 0

        # result, selected index
        res = 0

        # iterate over all the values in self.nums
        for i, value in enumerate(self.nums):
            if value == target:
                # target value is found, increment the number of found samples
                num_found_samples += 1

                # When having n_samples, replace reservoir with the probability of 1/n_samples
                if randint(1, num_found_samples) == 1:
                    res = i
        return res

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)