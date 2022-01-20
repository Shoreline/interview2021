# /*
#  * DFS
#  *
#  * How to avoid repeatedly adding duplicate groups:
#  *
#  * -> When sees duplicated elements (say 2), let 2; 2,2; 2,2,2;... can only
#  * show once each, and in the same child branch of '2'
#  *
#  * -> So in each branch (one "round" of DFS), if from S[pos] to
#  * S[S.length-1] there are duplicates, only allow the fist one (S[pos]) to
#  * be added to tmp list
#  *
#  * The rest is the same with subset I
#  */
# Note: need to sort nums first.
# time: O(n * 2^n) : dfs is called 2^n times, each time a deep copy takes O(n)
# space: O(n) : recursion stack is at most O(n) deep. (output storage is not considered)
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def dfs(tmp: List[int], pos: int):
            res.append(tmp[:])

            for i in range(pos, len(nums)):
                # each round, only process the first one of the duplicated chars
                # Next round, will process the 2nd of the duplicated chars, and so on so forth
                if i > pos and nums[i] == nums[i - 1]:
                    continue

                tmp.append(nums[i])
                dfs(tmp, i + 1)
                tmp.pop()

            return

        nums.sort()
        res = []
        dfs([], 0)
        return res;