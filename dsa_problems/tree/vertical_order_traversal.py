# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

from collections import deque

class Solution:
    
	def verticalOrderTraversal(self, root):
        result = []
        if root is None:
            return result
        HM = {}
        minL, maxL = 0, 0
        queue = deque()
        queue.append((root, 0))

        while len(queue) > 0:
            curr, vl = queue.popleft()
            if vl not in HM:
                HM[vl] = []
            HM[vl].append(curr.val)
            minL = min(minL, vl)
            maxL = max(maxL, vl)
            if curr.left:
                queue.append((curr.left, vl-1))
            if curr.right:
                queue.append((curr.right, vl+1))
        for vl in range(minL, maxL + 1):
            result.append(HM[vl])
        return result
