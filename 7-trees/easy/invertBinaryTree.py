from typing import Optional

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

# Recursive solution | Time Complexity: O(n), Space Complexity : O(n)
class Solution:
  def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    # base case
    if not root: return None

    # swap children
    root.right, root.left = root.left, root.right

    self.invertTree(root.left)
    self.invertTree(root.right)

    return root
      