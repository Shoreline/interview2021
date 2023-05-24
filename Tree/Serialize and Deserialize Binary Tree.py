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


# Follow up: n-ary tree (not just binary)

# Serialize with preorder traversal where sentinel "#" indicates the final child of a node has been processed,
# so the function returns to its parent call. Deserialize by creating a deque (could also use an iterator with next()
# instead of popleft()).

# While the next item is not "#", create a child with the item, add the child to the list of children and recurse to
# create its subtree. Repeat until there are no more children, then ignore the "#".

class Codec:
    def serialize(self, root):
        serial = []
        def preorder(node):
            if not node:
                return

            serial.append(str(node.val))

            for child in node.children:
                preorder(child)

            serial.append("#")      # indicates no more children, continue serialization from parent

        preorder(root)
        return " ".join(serial)

    def deserialize(self, data):
        if not data:
            return None

        tokens = deque(data.split())
        root = Node(int(tokens.popleft()), [])

        def helper(node):

            if not tokens:
                return

            while tokens[0] != "#": # add child nodes with subtrees
                value = tokens.popleft()
                child = Node(int(value), [])
                node.children.append(child)
                helper(child)

            tokens.popleft()        # discard the "#"

        helper(root)
        return root