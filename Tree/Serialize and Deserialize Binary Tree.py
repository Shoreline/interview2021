# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 1. Tree serialization: BFS or DFS
# 2. For DFS of a binary tree, we know three ways: pre/in/post order traversal
# 3. Pick DFS pre-order traversal. Since it also saves linkage sequences
# list.pop() costs O(1)

# Pre-order to serialize, reversed-pre-order to deserialize.
class Codec:
    def serialize(self, root):
        def preorder(root, tmp: list[str]):
            if not root:
                tmp.append('None,')
            else:
                tmp.append(str(root.val) + ',')
                preorder(root.left, tmp)
                preorder(root.right, tmp)

        res = []
        preorder(root, res)
        return ''.join(res)

    def deserialize(self, data: string):
        def reversed_preorder(data_list: list[string]):
            if data_list[-1] == 'None':
                data_list.pop()
                return None

            node = TreeNode(data_list.pop())
            node.left = reversed_preorder(data_list)
            node.right = reversed_preorder(data_list)

            return node

        # data list is reversed!
        # reversed(data) is not a list, but a list_reverseiterator object!
        # data.split(',').reverse() is also wrong, since it does not return a list!
        return reversed_preorder(data.split(',')[::-1])

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))