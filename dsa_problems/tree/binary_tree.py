
# Definition for a  binary tree node

class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	
	def isBalanced(self, A):
        self.result = 1
        self.isBalancedUtils(A)
        return self.result


    def isBalancedUtils(self, root):
        if root is None:
            return -1
        left_h = self.isBalancedUtils(root.left)
        right_h = self.isBalancedUtils(root.right)
        if abs(left_h - right_h) > 1:
            self.result = 0
        return 1 + max(left_h, right_h)


    def height(self, root):
    	if root is None:
    		return -1

    	left_h = self.height(root.left)
    	right_h = self.height(root.right)
    	return 1 + max(left_h, right_h)



    def size(self, root):
    	if root is None:
    		return 0

    	left_size = self.size(root.left)
    	right_size = self.size(root.right)
    	return 1 + left_size + right_size


    def mirror(self, root):
    	if root == None:
    		return None
    	_left = self.mirror(root.left)
    	_right = self.mirror(root.right)
    	root.left = _right
    	root.right = _left
    	return root


    def isValidBST(self, root, minV=-sys.maxsize, maxV=sys.maxsize): # is valid BST
        if root is None:
            return 1
        if (minV <= root.val) and (root.val <= maxV):
            isLeftValid = self.isValidBST(root.left, minV, root.val-1)
            isRightValid = self.isValidBST(root.right, root.val+1, maxV)
            return isLeftValid & isRightValid
        else:
            return 0
