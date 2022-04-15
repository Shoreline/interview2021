# counter<prefix_sum, show_up_times>
# nums can have negative elements
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counter = Counter({
                              0: 1})  # Normally, initialize prefix_sum map with 0:1 (so once targetSum = curPrefixSum we have a k-v pair in the map)
        ans = 0
        prefix_sum = 0
        for num in nums:
            prefix_sum += num
            if prefix_sum - k in counter:
                ans += counter[prefix_sum - k]
            counter[prefix_sum] += 1

        return ans
