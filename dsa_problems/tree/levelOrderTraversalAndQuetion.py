# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None


from collections import deque

class LevelOrderTraversal:


	def levelOrderTraversal(self, root):
        result = []
        queue = deque()
        queue.append(root)
        while len(queue) > 0:
            curr_level = []
            size = len(queue)
            while size > 0:
                curr = queue.popleft()
                curr_level.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                size -= 1
            result.append(curr_level)
        return result



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


    def zigzagLevelOrder(self, root):
        result = []
        if root is None:
            return result
        queue = deque()
        queue.append(root)
        left_to_right = True
        while len(queue) > 0:
            size = len(queue)
            level = []
            for i in range(size):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                if left_to_right:
                    level.append(curr.val)
                else:
                    level = [curr.val] + level
            result.append(level)
            left_to_right = not left_to_right
        return result


    def oddEvenLevelSumDifference(self, root):
        if root is None:
            return -1
        queue = deque()
        queue.append(root)
        is_level_odd = True
        odd_level_sum = 0
        even_level_sum = 0
        while len(queue) > 0:
            size = len(queue)
            for i in range(size):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                if is_level_odd:
                    odd_level_sum += curr.val
                else:
                    even_level_sum += curr.val
            is_level_odd = not is_level_odd
        return odd_level_sum - even_level_sum
