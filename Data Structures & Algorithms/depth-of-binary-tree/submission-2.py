# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # If the root is empty, there is no depth
        if not root:
            return 0
        
        # Now lets make a counter and also a queue to store the nodes going through

        nodes = deque()
        levels = 0
        nodes.append(root)

        while nodes:
            for i in range(len(nodes)):
                # Lets pop the node from the queue and store it inside of a node variable
                node = nodes.popleft()
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
            levels += 1
        return levels