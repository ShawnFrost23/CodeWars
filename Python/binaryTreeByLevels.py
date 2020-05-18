def tree_by_levels(node):
    if node is None:
        return []
    q = []
    list = []
    q.append(node)
    while q:
        count = len(q)
        while count > 0:
            tempNode = q.pop(0)
            list.append(tempNode.value)
            if tempNode.left:
                q.append(tempNode.left)
            if tempNode.right:
                q.append(tempNode.right)
            count -= 1
        
    return list

# You are given a binary tree:

# class Node:
#     def __init__(self, L, R, n):
#         self.left = L
#         self.right = R
#         self.value = n
# Your task is to return the list with elements from tree sorted by levels, which means the root element goes first, then root children (from left to right) are second and third, and so on.

# Return empty list if root is None.

# Example 1 - following tree:

#                  2
#             8        9
#           1  3     4   5
# Should return following list:

# [2,8,9,1,3,4,5]
# Example 2 - following tree:

#                  1
#             8        4
#               3        5
#                          7
# Should return following list:

# [1,8,4,3,5,7]