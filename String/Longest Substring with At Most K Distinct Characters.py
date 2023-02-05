# Sliding window
# T: O(n); S: O(k)
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if not s or k == 0:
            return 0

        char_count = collections.defaultdict(int)  # map<char, count> in the sliding window
        start, end = 0, -1
        res = 0
        for i, c in enumerate(s):
            char_count[c] += 1
            end += 1

            if len(char_count) > k:
                for j in range(start, i):
                    char_count[s[j]] -= 1
                    if char_count[s[j]] == 0:
                        del char_count[s[j]]
                        start = j + 1
                        break
            res = max(res, end - start + 1)

        return res

    # T: O(n*k)
# S: O(k)
# class Solution:
#     def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
#         if k == 0 or len(s) == 0:
#             return 0

#         char_pos = {s[0]:0} # the last shown index of a char in current sliding window
#         start, end = 0, 0
#         res = 1
#         for i in range(1, len(s)):
#             char_pos[s[i]] = i
#             end += 1

#             if len(char_pos) > k: # Need to reduce the sliding window from left, to where it can exclude one existing character
#                 min_idx = float('inf')
#                 for c in char_pos:
#                     min_idx = min(min_idx, char_pos[c])
#                 char_pos.pop(s[min_idx])
#                 start = min_idx + 1

#             res = max(res, end - start + 1)

#         return res


#     public class Solution {
# 	public int lengthOfLongestSubstringTwoDistinct(String s) {
# 	    Map<Character, Integer> map = new HashMap<>();
# 	    int maxLen = 0;
# 	    int left = 0;
# 	    for (int right = 0; right < s.length(); right++) {
# 		char c = s.charAt(right);
# 		if (!map.containsKey(c)) {
# 		    map.put(c, 0);
# 		}
# 		map.put(c, map.get(c) + 1);

# 		if (map.size() > 2) {
# 		    for (int i = left; i < right; i++) {
# 			char tmp = s.charAt(i);
# 			if (map.get(tmp) == 1) {
# 			    map.remove(tmp);
# 			    left = i + 1;
# 			    break;
# 			} else {
# 			    map.put(tmp, map.get(tmp) - 1);
# 			}
# 		    }
# 		}

# 		maxLen = Math.max(maxLen, right - left + 1);
# 	    }
# 	    return maxLen;

# 	}
#     }
