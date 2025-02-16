class Solution:
	# @param A : root node of tree
	# @return a list of integers
	def preorderTraversal(self, A):
        self.result = []
        # self.recursivePreorder(A) # Recursive preorder traversal using stack TC = O(N), SC = O(H)
        # self.iterativePreorder(A) # Iterative preorder traversal using stack TC = O(N), SC = O(H)
        self.morrisPreorder(A)  # Morris preorder traversal:  TC = O(N), SC = O(1)
        return self.result
        
    
    def morrisPreorder(self, root):
        curr = root
        while curr is not None:
            if curr.left is None:
                self.result.append(curr.val)
                curr = curr.right   
            else:
                temp = curr.left
                if temp is not None:
                    while not (temp.right is None or temp.right is curr):
                        temp = temp.right
                if temp.right is None:
                    self.result.append(curr.val)
                    temp.right = curr
                    curr = curr.left
                else:
                    temp.right = None
                    curr = curr.right

    def iterativePreorder(self, root):
        stack = []
        stack.append(root)
        while len(stack) > 0:
            curr = stack.pop()
            self.result.append(curr.val)
            if curr.right is not None:
                stack.append(curr.right)
            if curr.left is not None:
                stack.append(curr.left)
    
    def recursivePreorder(self, root):
        if root is None:
            return
        self.result.append(root.val)
        self.recursivePreorder(root.left)
        self.recursivePreorder(root.right)