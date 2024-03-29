# Bucket sort
# maximum gap is surely >= (max(nums) - min(nums) // (len(nums) - 1) -> bucket_size
# Make len(nums) buckets to put elements in nums. But we only need to save min/max value in each bucket, instead of
# bucket_size number of values.

# Suppose in our integer array N elements, the min value is min and the max value is max. Then the maximum gap will be
# greater or equal to ceiling[(max - min ) / (N - 1)].
#
# Let bucketSize = ceiling[(max - min ) / (N - 1)].
#
# We divide all numbers in the array into N buckets, each bucket has size of bucketSize, where i-th (zero-based index)
# bucket contains all numbers in range [min + i*bucketSize, min + (i+1)*bucketSize).
#
# Because maximum gap is always greater or equal to bucketSize so in each bucket, we only need to store max element and
# min element, skip middle elements (min < middle < max) in the same bucket.
#
# Finally, we only need to compare max number in current bucket and min number in next bucket to get the relatively
# large gap and find out which two buckets have the maximum gap.
import math


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        mi, ma, n = min(nums), max(nums), len(nums)
        if mi == ma:
            return 0  # All elements are the same

        bucketSize = math.ceil((ma - mi) / (n - 1))  # the avg gap of elements in the input array
        # Simply use two arrays to save min/max values in a bucket
        bucket_mins = [math.inf] * n  # don't use bucketSize, which can be huge when n is small. eg nums = [1, 99999]
        bucket_maxs = [-math.inf] * n
        for x in nums:  # Put each element in nums into its bucket
            idx = (x - mi) // bucketSize
            bucket_mins[idx] = min(bucket_mins[idx], x)
            bucket_maxs[idx] = max(bucket_maxs[idx], x)

        max_gap = 0  # Maximum gap is always greater or equal to bucketSize (avg gap)
        pre_max = bucket_maxs[0]  # We always have 0th bucket
        for i in range(1, n):
            if bucket_mins[i] == math.inf:
                continue  # Skip empty bucket

            # No need to compare min/max values within the same bucket, which is <= bucketSize
            max_gap = max(max_gap, bucket_mins[i] - pre_max)
            pre_max = bucket_maxs[i]
        return max_gap
