# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [p,q]
        while stack:
            n,m = stack.pop(), stack.pop()
            if n is None and m is None:
                continue
            if n is None or m is None or n.val != m.val:
                return False
            stack += n.left,m.left,n.right,m.right
        return True
