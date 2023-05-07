# Each node has two pointers:
#    one to the next node in the same level
#    the other to the its counterpart (node with same value) in the next level
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.down = None


class Skiplist:
    def __init__(self):
        self.levels = []
        prev = None
        for i in range(16):  # estimated nodes shall <= 2 ^ 16
            node = Node(-math.inf)
            self.levels.append(node)
            if prev:
                prev.down = node
            prev = node

    # For each level, find the maximum node that node.val < target
    # Then after reaching the bottom level, if target node exist, it will be res[-1].next
    def _iter(self, target):
        res = []
        node = self.levels[0]
        while node:
            while node.next and node.next.val < target:
                node = node.next

            res.append(node)
            node = node.down
        return res

    def search(self, target: int) -> bool:
        itr_res = self._iter(target)
        return itr_res and itr_res[-1].next and itr_res[-1].next.val == target

    def add(self, num: int) -> None:
        itr_res = self._iter(num)
        prev = None  # counterpart node of one level deeper
        for i in range(len(itr_res) - 1, -1, -1):
            node = Node(num)
            node.next, node.down = itr_res[i].next, prev
            itr_res[i].next = node
            prev = node

            # Keep a 1/2 chance of countinue adding this value to one level upper
            if random.random() > 0.5:
                break

    # If num to be ereased does not exist, returns False
    def erase(self, num: int) -> bool:
        itr_res = self._iter(num)
        # If not found, just return False
        #   - same as calling self.search(num)
        if not (itr_res and itr_res[-1].next and itr_res[-1].next.val == num):
            return False

        # If found, erease this node from every level
        for pre_node in itr_res:
            if pre_node.next and pre_node.next.val == num:
                pre_node.next = pre_node.next.next
        return True

# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)