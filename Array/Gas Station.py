# No need to handle circle.
# 把这个圈划分成一个个的负序列，以及一个正序列（如果存在的话）。从任意一个站出发，我们可以累加油的净余量，如果出现负的，序列结束，开启一个新的，并且证明旧的这个序列的起点不能作为起点，因为会出现负油量，不能继续前进。
# 下面我们证明 "不仅这个负序列的起点不能作为起点，负序列中的任意一点都不能作为起点"
# 证明： 假设我们取定负序列中的一个站作为起点，因为一个序列一旦遇到负的净余量就会结束并且开启新的，那么说明在这个起点前的累加结果必然是正数（否则会结束这个序列，则前面不会是这个序列的一部分）。如此我们从当前序列出发必然会使走到序列终点时负的油量更大，本来已经是负的，所以不能去负序列的任意一个结点作为起点。

# 根据上面的划分方式，我们会把圈分成一段段的序列，而且其中最多只有一个正序列，那就是绕一圈回到起点的那个序列（当然也有可能整个圈是一个正序列，就是油量一直为正，那么我们测的开始点就可以作为起点了）。接下来我们证明
# 如果将全部油量累计起来，总量为正，那么一定能找到一个起点，使得可以走完一圈，也就是一定有解。

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas, total_cost = gas[0], cost[0]
        cur_gas = gas[0]
        start_station = 0

        for i in range(1, len(gas)):
            if cur_gas >= cost[i - 1]:  # have enough gas to reach gas[i]
                cur_gas = cur_gas - cost[i - 1] + gas[i]
            else:  # Can't reach gas[i]. Reset, let gas station i to be the start of new positive sequence
                cur_gas = gas[i]
                start_station = i

            total_gas += gas[i]
            total_cost += cost[i]

        return start_station if total_gas >= total_cost else -1
