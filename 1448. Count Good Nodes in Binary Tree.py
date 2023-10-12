""""Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.
Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.
 

Example 1:"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, val):
            if not root:
                return 0
            if root.val >= val:
                self.count += 1
            dfs(root.left, max(val, root.val))
            dfs(root.right, max(val, root.val))
        self.count = 0
        dfs(root, root.val)
        return self.count

#     res = 1 if node.val >= maxVal else 0
#     maxVal = max(maxVal, node.val)
#     res += dfs(node.left, maxVal)
#     res += dfs(node.right, maxVal)
#     return res


"""
sent the max of current root value or current path value to children"""
