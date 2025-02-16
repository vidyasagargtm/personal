# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : root node of tree
	# @return a list of integers
	def postorderTraversal(self, A):
        self.result = []
        # self.recursivePostorder(A)
        self.iterativePostorder(A)
        self.morrisPostorder(A)
        return self.result

    def recursivePostorder(self, root):
        if root is None:
            return
        self.recursivePostorder(root.left)
        self.recursivePostorder(root.right)
        self.result.append(root.val)
    
    def iterativePostorder(self, root):
        stack = [root]
        while len(stack) > 0:
            curr = stack.pop()
            self.result.append(curr.val)
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
        start, end = 0, len(self.result) - 1
        while start < end:
            self.result[start], self.result[end] = self.result[end], self.result[start]
            start += 1
            end -= 1
    

    # def morrisPostorder(self, root):
    #     curr = root
    #     while curr:
    #         if curr.left is None:
    #             pass


        
