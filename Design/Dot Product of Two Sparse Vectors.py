# Because the vector is sparse, use a data structure that stores the index and value where the element is nonzero.
# Use a list of index, value pairs: [[index1, value1], [index2, value2], ...]
# Although we can also use a hashset to only save the non-zero (index, value) items -> but hashing/lookup will be slow for super large sparse vectors

# Time: O(n) for SparseVector(nums1); O(L1 + L2) for dotProduct()
# Space: O(L) and O(1), respectively
class SparseVector:
    def __init__(self, nums: List[int]):
        self.present_items = []  # list<[index, val]>
        for i in range(len(nums)):
            if nums[i] != 0:
                self.present_items.append([i, nums[i]])

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        i, j = 0, 0
        while i < len(self.present_items) and j < len(vec.present_items):
            if self.present_items[i][0] == vec.present_items[j][0]:  # if indice match with each other
                res += self.present_items[i][1] * vec.present_items[j][1]
                i += 1
                j += 1
            elif self.present_items[i][0] < vec.present_items[j][0]:  # increment i or j (check next possible match)
                i += 1
            else:
                j += 1

        return res

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)