# Every worker can be assigned at most one job, but one job can be completed multiple times.

# Solution 1
# zip difficulty and profit as jobs.
# sort jobs and sort 'worker'.
# Use 2 pointers. For each worker, find his maximum profit best he can make under his ability.
# Because we have sorted jobs and worker,
# we will go through two lists only once.
# this will be only O(D + W).
# O(DlogD + WlogW), as we sort jobs.

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # jobs = [[d1, p1], [d2, p2], ... ]. Sorted by 1) difficulti; 2) profit
        jobs = sorted(zip(difficulty, profit))
        res = i = best = 0

        # sort worker by ability as well. Avoid checking incapable tasks.
        for ability in sorted(worker):
            while i < len(jobs) and ability >= jobs[i][0]:
                best = max(jobs[i][1], best)
                i += 1
            res += best
        return res