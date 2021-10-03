"""
Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.
"""
class Solution:
    def flatten(self, root: TreeNode) -> None:
        def find(root):
            if not root:
                return
            l,r=find(root.left),find(root.right)
            if not l:
                root.right=r
                return root
            else:
                root.right=l
                root.left=None
                x=root
                while x.right:
                    x=x.right
                x.right=r
                return root
        find(root)
