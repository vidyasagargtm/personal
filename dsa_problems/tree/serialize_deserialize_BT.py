# Definition for a  binary tree node

from collections import deque

class TreeNode:

   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None


class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def serialize(self, root):
        result = []
        if root is None:
            return result
        result.append(root.val)
        queue = deque()
        queue.append(root)
        while len(queue) > 0:
            curr = queue.popleft()
            if curr.left:
                result.append(curr.left.val)
                queue.append(curr.left)
            else:
                result.append(-1)
            if curr.right:
                result.append(curr.right.val)
                queue.append(curr.right)
            else:
                result.append(-1)
        return result


    def deserialize(self, arr):
        N = len(arr)
        if N < 1:
            return None

        root = TreeNode(arr[0])
        index = 1
        queue = deque()
        queue.append(root)

        while len(queue) > 0:
            curr = queue.popleft()
            if arr[index] != -1:
                new_node = TreeNode(arr[index])
                curr.left = new_node
                queue.append(curr.left)


            if arr[index + 1] != -1:
                new_node = TreeNode(arr[index+1])
                curr.right = new_node
                queue.append(curr.right)
            index += 2
        return root



A = [1, 2, 3, 4, 5, -1, -1, -1, -1, -1, -1]
obj = Solution()
root = obj.deserialize(A)
def recursiveInorder(root):
    if root is None:
        return 
    recursiveInorder(root.left)
    print(root.val, end=' ')
    recursiveInorder(root.right)
recursiveInorder(root)

print("")
print(obj.serialize(root))



