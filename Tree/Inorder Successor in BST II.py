class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Optional[Node]':
        if not node:
            return None

        # if has right subtree, return the leftmost leaf of the right subtree
        if node.right:
            node = node.right
            while node.left:
                node = node.left
            return node

        # if has parent,
        #   if this node is the left child of parent, return parent
        #   Otherwise keep going up to parent's parent
        while node.parent:
            if node == node.parent.left:
                return node.parent
            node = node.parent

        return None