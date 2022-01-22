# Just sort the array first, then greedy
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)

        res = 0
        for box_type in boxTypes:
            size = box_type[0] if truckSize >= box_type[0] else truckSize
            res += box_type[1] * size
            truckSize -= size
            if truckSize == 0:
                break

        return res