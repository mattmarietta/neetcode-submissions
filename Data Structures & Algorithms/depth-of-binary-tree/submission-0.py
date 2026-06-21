# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # BFS 
        # 1 -> 2, 3 -> null, null, 4, null
        # return 3 
        
        if root == None:
            return 0
        # Initialize a queue and push the root
        bang = deque()
        bang.append(root)
        # Append whole root


        level = 0
        while bang:
            # While the queue is still full
            for i in range(len(bang)):
                node = bang.popleft()
                if node.left:
                    bang.append(node.left)
                if node.right:
                    bang.append(node.right)
            level += 1
        return level
            




