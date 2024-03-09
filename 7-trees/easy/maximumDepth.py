from typing import Optional

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def maxDepth(self, root: Optional[TreeNode], depth = 0) -> int:
    if not root:
      return depth

    leftDepth = self.maxDepth(root.left, depth + 1)
    rightDepth = self.maxDepth(root.right, depth + 1)

    return max(leftDepth, rightDepth)