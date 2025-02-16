# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : root node of tree
	# @return a list of integers
	def inorderTraversal(self, A):
        self.result = []
        # self.recursiveInorder(A)
        self.iterativeInorder(A)
        # self.morrisInorder(A)
        return self.result

    def morrisInorder(self, root):
        curr = root
        while curr:
            if not curr.left:
                self.result.append(curr.val)
                curr = curr.right
            else:
                temp = curr.left
                if temp:
                    while not (temp.right == None or temp.right == curr):
                        temp = temp.right
                if temp.right == None:
                    temp.right = curr
                    curr = curr.left
                else:
                    temp.right = None
                    self.result.append(curr.val)
                    curr = curr.right
    
    def iterativeInorder(self, root):
        stack = []
        curr = root
        while len(stack) > 0 or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            self.result.append(curr.val)
            curr = curr.right



    def recursiveInorder(self, root):
        if root is None:
            return 
        self.recursiveInorder(root.left)
        self.result.append(root.val)
        self.recursiveInorder(root.right)
        