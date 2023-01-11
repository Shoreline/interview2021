# Push all possible k smallest elements in a heap, and do k pops.
#   Note that we may need to push more than k elements.
#
# Nature thought: max heap. But this time the input array is not random, but sorted in some way.
# So, our thought is to use a min heap, and pop k elements.

# the total time complexity for this algorithm comes down to be O(X+Klog(X)) where X is min(K, N). N: len(matrix), the
# number of sorted lists.
# Since all rows/columns are already sorted, only need to check a subset of elements in matrix

# min-heap will contain a triplet of (val, row, column)
# It's important to know what row and column an element belongs to. Without knowing that, we won't be able to move
# forward in that particular list. So, apart from adding an element to the heap, we also need to add its row and column
# number.

# Say the minimum triplet in the heap is (v, r, c), then when it is pop out, which triplet to add to the heap?
#   - The next triplet doesn't HAVE to be the next minium element in matrix. It shall be the next POSSIBLE min element
#   - It shall be (v2, r, c+1).  (Why not (v2', r+1, c)? actually that may also work)
#   - No need to ever increment r. The heappush() will do that while finding the minimum triplet

import heapq

# Maintain a min_heap that always has the smallest element.
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # Its size does not need to be k. Our goal is not to KEEP the k smallest elements in it. But to POP smallest
        # element K times.
        min_heap = []
        # Also, the size of min_heap doesn't need to be a constant

        for row in range(min(k, len(matrix))):
            min_heap.append((matrix[row][0], row, 0))  # triplet: val, row, column
        # heapq.heapify(min_heap)

        # while we haven't poped the smallest element k times
        for i in range(k):
            val, row, column = heapq.heappop(min_heap)  # not triplet = heapq.heappop(min_heap)
            if column < len(matrix) - 1:
                heapq.heappush(min_heap, (matrix[row][column + 1], row, column + 1))

        return val  # Python variable has intresting life scope