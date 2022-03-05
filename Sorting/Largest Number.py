# sorting problem.
# sort n1 and n2 by each digit
# - can also be done by let x and y be numbers in string format. And compare their concatenated results
# Note that python3 does not support cmp = compare in sort() anymore (can workaround by import functools)

class LargerNumKey(str):
    def __lt__(x: str, y: str):
        return x + y > y + x  # x and y are numbers in string format. Here are compare their concatenated results


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        # return '0' if largest_num[0] == '0' else largest_num # largest_num can be "00"

        nums_str = [str(num) for num in nums]
        nums_str.sort(key=LargerNumKey)
        if nums_str[0] == '0':
            return '0'
        else:
            return ''.join(nums_str)

# public class LargestNumber {
#     public class Solution {
# 	public String largestNumber(int[] nums) {
# 	    if (nums == null || nums.length == 0) {
# 		return "";
# 	    }

# 	    Integer[] nums2 = new Integer[nums.length];
# 	    for (int i = 0; i < nums.length; i++) {
# 		nums2[i] = nums[i];
# 	    }

# 	    Arrays.sort(nums2, new Comparator<Integer>() {
# 		@Override
# 		public int compare(Integer i1, Integer i2) {
# 		    String s1 = String.valueOf(i1);
# 		    String s2 = String.valueOf(i2);
# 		    return -(s1 + s2).compareTo(s2 + s1);
# 		}
# 	    });

# 	    StringBuilder res = new StringBuilder();
# 	    for (int i = 0; i < nums2.length; i++) {
# 		// avoid cases like "00".
# 		if (res.length() == 0 && nums2[i] == 0 && i < nums2.length - 1 && nums2[i] == nums2[i + 1]) {
# 		    continue;
# 		}
# 		res.append(String.valueOf(nums2[i]));
# 	    }

# 	    return res.toString();
# 	}
#     }

# }