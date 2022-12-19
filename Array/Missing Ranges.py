# We are told that all elements in nums are within [lower, higher]
# /*
#  * cannot just do "if not nums return []" at the beginning, but return [lower -> upper]
#  */
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        nums = [lower - 1] + nums + [upper + 1]  # Add lower_bound and upper_bond elements to nums
        res = []

        # Only react when there is a gap (nums[i+1] - nums[i] > 1)
        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] == 2:  # Gap is only 1, so no need to use "->"
                res.append(str(nums[i] + 1))
            elif nums[i + 1] - nums[i] > 2:  # Gap is more than 1, need to use "->"
                res.append(str(nums[i] + 1) + '->' + str(nums[i + 1] - 1))

        return res

# 	public List<String> findMissingRanges(int[] nums, int lower, int upper) {
# 	    List<String> res = new ArrayList<String>();

# 	    int cur = lower;
# 	    for (int i = 0; i < nums.length; i++) {
# 		if (cur < nums[i]) {
# 		    if (cur < nums[i] - 1) {
# 			// "->" is a String so no need to cast other Integers
# 			res.add(cur + "->" + (nums[i] - 1));
# 		    } else {
# 			res.add(String.valueOf(cur));
# 		    }
# 		    cur = nums[i] + 1;
# 		} else if (cur == nums[i]) {
# 		    cur++;
# 		}
# 	    }

# 	    if (cur == upper) {
# 		res.add(String.valueOf(cur));
# 	    } else if (cur < upper) {
# 		res.add(cur + "->" + upper);
# 	    }

# 	    return res;
# 	}    