# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : list of integers
	# @param B : list of integers
	# @return the root node in the tree
	def buildTree(self, A, B):
        self.HM = {ele: index for index, ele in enumerate(A)}
        N = len(A) - 1
        return self.buildTreeUtils(A, 0, N, B, 0, N)



    # Build binary tree from given inorder and postorder
    def buildTreeUtils(self, ino, s1, e1, post, s2, e2):
        if s1 > e1:
            return None
        root = TreeNode(post[e2])
        index = self.HM[post[e2]]
        count = index - s1

        lst_s1 = s1
        lst_e1 = index - 1

        lst_s2 = s2
        lst_e2 = s2 + count - 1


        rst_s1 = index + 1
        rst_e1 = e1

        rst_s2 = s2 + count
        rst_e2 = e2 - 1
        root.left = self.buildTreeUtils(ino, lst_s1, lst_e1, post, lst_s2, lst_e2)
        root.right = self.buildTreeUtils(ino, rst_s1, rst_e1, post, rst_s2, rst_e2)
        return root


    # Build binary tree from given preorder and inorder
    def buildTreeUtils(self, pre, s1, e1, ino, s2, e2):
        if s1 > e1:
            return None

        root = TreeNode(pre[s1])
        index = self.HM[pre[s1]]
        count = index - s2

        lst_s1 = s1 + 1
        lst_e1 = s1 + count
        lst_s2 = s2
        lst_e2 = index - 1

        rst_s1 = s1 + count + 1
        rst_e1 = e1
        rst_s2 = index + 1
        rst_e2 = e2

        root.left = self.buildTreeUtils(pre, lst_s1, lst_e1, ino, lst_s2, lst_e2)
        root.right = self.buildTreeUtils(pre, rst_s1, rst_e1, ino, rst_s2, rst_e2)

        return root
        