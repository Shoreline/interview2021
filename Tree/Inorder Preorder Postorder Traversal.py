# Recursion methods
def inorderTraversal(root: TreeNode) -> List[int]:
    def helper(root: TreeNode):
        if root:
            helper(root.left)
            res.append(root.val)
            helper(root.right)

    res = []
    helper(root)
    return res


def preorderTraversal(root: Optional[TreeNode]) -> List[int]:
    def helper(root: TreeNode):
        if root:
            res.append(root.val)
            helper(root.left)
            helper(root.right)

    res = []
    helper(root)
    return res


# Iterative methods
def inorderTraversal2(root: TreeNode) -> List[int]:
    res = []
    stack = []
    cur = root
    while cur or stack:
        if not cur:
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        else:
            stack.append(cur)  # not cur.left nor cur.right!
            cur = cur.left

    return res


def preorderTraversal2(root: Optional[TreeNode]) -> List[int]:
    res = []
    stack = []
    cur = root
    while cur or stack:
        if not cur:
            cur = stack.pop()
        res.append(cur.val)
        if cur.right:
            stack.append(cur.right)
        cur = cur.left
    return res


def postorderTraversal2(root: Optional[TreeNode]) -> List[int]:
    res = []
    stack = []
    cur = root
    while cur or stack:
        if not cur:
            cur = stack.pop()
        res.append(cur.val)
        if cur.left:
            stack.append(cur.left)
        cur = cur.right

    return reversed(res)


def preorderTraversal3(root: Optional[TreeNode]) -> List[int]:
    res = []
    stack = [root]

    while stack:
        root = stack.pop()
        if root:
            res.append(root.val)

            # First push the node you want to pop later
            stack.append(root.right)
            stack.append(root.left)

    return res


def postorderTraversal3(root: Optional[TreeNode]) -> List[int]:
    res = []
    stack = [root]

    while stack:
        root = stack.pop()
        if root:
            res.append(root.val)
            stack.append(root.left)
            stack.append(root.right)

    return reversed(res)
