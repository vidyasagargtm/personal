# Definition for a  binary tree node

from collections import deque


class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None


class BinaryTreeViews:
    
    def leftView(self, root):
        result = []
        if root is None:
            return result
        queue = deque()
        queue.append(root)
        while len(queue) > 0:
            size = len(queue)
            for i in range(size):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append((curr.right))
                if i == 0:
                    self.result.append(curr.val)
        return result


    def rightView(self, root):
        result = []
        if root is None:
            return result
        queue = deque()
        queue.append(root)
        while len(queue) > 0:
            size = len(queue)
            for i in range(size):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append((curr.right))
                if i == (size-1):
                    result.append(curr.val)
        return result

