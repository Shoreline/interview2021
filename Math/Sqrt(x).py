# lgN binary search
# I think this problem's key point is that we want to find the largest number, which num <= x/num, therefore we should
# use the binary search to find the upper bound within the range(1,x).
class Solution:
    def mySqrt(self, x: int) -> int:
        low, high = 1, x
        res = 0
        while low <= high:
            mid = low + (high - low) // 2
            # Do not use if(mid*mid==x), may exceed Integer limit
            if mid == x // mid:
                return mid
            # upper bound的形式，因为我们要找的ans要是最接近于x的最大的数，利用upper bound
            elif mid < x // mid:  # mid still have possibility to grow
                res = mid
                low = mid + 1
            else:
                high = mid - 1

        return res  # or return low - 1

# class Solution:
#     def mySqrt(self, x: int) -> int:
#         low = 1
#         high = x // 2 + 1 # we know res*res <= x, so res <= x//2 + 1
#         while low <=high:
#             # Do not use if(mid*mid==x), may exceed Integer limit
#             mid = (low + high) // 2
#             if mid == x // mid:
#                 return mid
#             elif mid < x // mid:
#                 low = mid + 1
#             else:
#                 high = mid - 1

#         return high # not returning low!

#     /*
#      * Newton's method, works when x is int
#      */
#     public class Solution {
# 	public int mySqrt(int x) {
# 	    if (x == 0) {
# 		return x;
# 	    }

# 	    double res = x / 2.0;
# 	    double preRes = 0;

# 	    while (res != preRes) {
# 		preRes = res;
# 		res = (res + x / res) / 2;
# 	    }

# 	    return (int) res;
# 	}
#     }