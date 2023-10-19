"""Given the root of a binary tree, return all root-to-leaf paths in any order.
A leaf is a node with no children.
Example 1
Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]
Example 2:

Input: root = [1]
Output: ["1"]"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []

        def backtrack(root, s):
            if root and not root.left and not root.right:
                s += str(root.val)
                res.append(s)
                return
            if not root:
                return

            s += str(root.val) + '->'
            backtrack(root.left, s)
            backtrack(root.right, s)
            s = s[:-3]
        backtrack(root, "")
        return res
