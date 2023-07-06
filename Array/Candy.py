# Each child must have at least one candy.

# Children with a higher rating get more candies than their neighbors.

# Go from left to right and while increase, give the the next person +1 candy from previous, if not, leave number of candies as it was. In this way when we make this pass we make sure that condition that person with bigger value gets more candies fulfilled for pairs of adjusent persons where left person is smaller than right. Now, go from right to left and do the same: now we cover pairs of adjacent persons where right is smaller than left. After these two passes all persons are happy.
class Solution:
    def candy(self, ratings: List[int]) -> int:
        R = ratings
        n = len(R)
        ans = [1] * len(R)  # at least one candy per child

        # if right neighbor has higher rating, +1 candy
        for i in range(n - 1):
            if R[i] < R[i + 1]:
                ans[i + 1] = max(1 + ans[i], ans[i + 1])

        # if left neighbor has higher rating, +1 candy
        for i in range(n - 2, -1, -1):
            if R[i + 1] < R[i]:
                ans[i] = max(1 + ans[i + 1], ans[i])

        return sum(ans)
