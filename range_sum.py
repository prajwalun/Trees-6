# The rangeSumBST method calculates the sum of values within [low, high] in a BST.

# Approach:
# - Traverse the tree using DFS.
# - Add node value to sum only if it's within range.
# - Recursively calculate left and right subtree sums.

# TC: O(n) - Visit each node once.
# SC: O(h) - Recursive stack depth (h = height of tree).


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node):
            if not node:
                return 0
            
            current_val = 0
            if low <= node.val <= high:
                current_val = node.val
            
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            
            return current_val + left_sum + right_sum
        
        return dfs(root)