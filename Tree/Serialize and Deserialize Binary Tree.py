# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 1. Tree serialization: BFS or DFS
# 2. For DFS of a binary tree, we know three ways: pre/in/post order traversal
# 3. Pick DFS pre-order traversal. Since it also saves linkage sequences
# list.pop(0) costs O(1)?
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

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
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def preorder(data_list: list[string]):
            if data_list[-1] == 'None':
                data_list.pop()
                return None

            node = TreeNode(data_list.pop())
            node.left = preorder(data_list)
            node.right = preorder(data_list)

            return node

        return preorder(data.split(',')[::-1])

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))