# Definition for a binary tree node.
# class TreeNode:
#   def __init__(self, x):
#       self.val = x
#       self.left = None
#       self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
    #make all children rights. this may not be in order
    
    #make checks and switch -- n2
    
    ##found out, use stack
    ##LIFO - last in, first out

    #check for bad input
    if root is None:
        return

    #create stack
    stack = []
    
    stack.append(root)
    #now we have the root, 1, in the stack

    while not stack.isEmpty():
        curr = stack.pop()
        if curr.right is not None:
            stack.push(curr.right)
        if curr.left is not None:
            stack.push(curr.left)
        if not stack.isEmpty():
            curr.right = stack.peek()

        curr.left = None
