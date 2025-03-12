# s = "I love india"
# search = "ind"

# word = s.split(" ")
# for index, string in enumerate(word):
#     if  len(string) > len(search) and string[len(search)] == search:
#         index += 1

# print(index + 1)

# Leetcode Problem: 1475. Final Prices With a Special Discount in a Shop
# def solution(nums):
#     res = []
#     i = 0
#     j = 1
#     while i < len(nums) and j < len(nums):
#         if nums[i] >= nums[j]:
#             res.append(nums[i] - nums[j])
#             i += 1
#             if i == j:
#                 j += 1 
#         else:
#             j += 1
#     if i < len(nums):
#         for num in range(i, len(nums)):
#             res.append(nums[num])

#     return res

# array = [1,6,3,4,5]
# print(solution(array))

# Sliding Window

# def solution(nums, k):
#     res = []
#     l = 0
#     sum = 0
#     for r in range(len(nums)):
#         sum += nums[r]
#         if r - l + 1 == k:
#             res.append(sum)
#             sum -= nums[l]
#             l += 1
#     while l < len(nums):
#         res.append(nums[l])
#         l += 1
#     return res

# array = [1,2,3,4,5,6,7]
# k = 3
# print(solution(array, k))

# Swap the string

# def solution(s):
#     l, r = 0, len(s) - 1
#     string = list(s)
    
#     while l < r:
#         string[l], string[r] = string[r], string[l]
#         l += 1
#         r -= 1
#     return "".join(string)

# name = "gurung"
# print(solution(name))


#Recursive 
# def recursion(num, total=0):
#     if num == 0:
#         return total
#     total += num
#     return recursion(num - 1, total)

# value = 5
# print(recursion(value))

# Pattern Searching

# def search_pattern(pattern, search):
#     n = len(pattern)
#     m = len(search)
#     res = []
#     for i in range(n - m + 1):
#         if pattern[i:i + m] == search:
#             res.append(i) 
    
#     return res
# text1 = "AABAACAADAABAABA"
# pattern1 = "AABA"
# print(search_pattern(text1, pattern1))



# Linked List

# class Node:
#     def __init__(self, data = None, next = None):
#         self.data = data
#         self.next = next
#         # print("Data and Next: ", data, next)

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def insert(self, data):
#         node = Node(data, self.head)
#         print("Node: ", node)
#         self.head = node
    
#     def print(self):
#         if self.head is None:
#             print("Empty") 
#             return 
        
#         itr = self.head
#         res = ""
#         while itr:
#             res += str(itr.data) + "-->"
#             itr = itr.next
#         print(res)
    
#     def reverse(self):
#         if self.head is None:
#             return
        
#         itr = self.head

# if __name__ == "__main__":
#     obj = LinkedList()
#     obj.insert(1)
#     obj.insert(2)
#     obj.insert(3)
#     obj.insert(4)
#     obj.insert(5) 
#     obj.print() 


#Binary Search 
# def binary_search(arr, k):
#     l = 0
#     r = len(arr)
#     while l < r:
#         m = ( l + r ) // 2
#         if arr[m] > k:
#             r = m
#         elif arr[m] < k:
#             l = m + 1
#         else:
#             return m
#     return -1

# arr = [1,2,3,4,5,6,7,8]
# search = 7
# print("Index: ", binary_search(arr, search))

#----------------------------------------------------
# class Node:
#     def __init__(self, Data=None, Next=None):
#         self.data = Data
#         self.next = Next

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def insert(self, data):
#         node = Node(data, self.head)
#         self.head = node

#     def display(self):
#         if self.head is None:
#             print("No data available")
#             return
#         itr = self.head
#         res = ""
#         while itr:
#             res += str(itr.data)
#             if itr.next:
#                 res += "-->"
#             itr = itr.next
#         print(res)

#     def reversed(self):
#         if self.head is None:
#             print("No data available to reverse")
#             return

#         prev = None
#         current = self.head

#         while current:
#             next_node = current.next  # Save the next node
#             current.next = prev      # Reverse the current node's pointer
#             prev = current           # Move `prev` to the current node
#             current = next_node      # Move to the next node

#         self.head = prev  # Update the head to the last node

#     def check_cycle(self):
#         slow, fast = self.head, self.head
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
#             if slow == fast:
#                 return True
#         return -1
    

# if __name__ == "__main__":
#     obj = LinkedList()
#     obj.insert(3)
#     obj.insert(5)
#     obj.insert(10)
#     print("Original LinkedList:")
#     obj.display()
#     print("Reversed: ")
#     obj.reversed()
#     obj.display()
#     print("Check for cycle: ", obj.check_cycle())

#---------------------------------------------------------------------

#Time complexity : 0(n)       |     o(n^2)
# def two_sum(arr, k):
#     j = 0

    

# if __name__ == "__main__":
#     array = [24, 90, 23, 14, 50, 40]
#     sum = 90
#     print(two_sum(array, sum))

#-----------------------------------------------------
# def get(n):
#     if n < 1: return
#     print(0)
#     get(n - 1)
#     print(0)
#     get(n - 3) 
#     print(n)

# print(get(3))

#--------------------------Tree------------------------------

# class TreeNode:
#     def __init__(self, val = None, left = None, right = None):
#         self.val = val
#         self.right = right
#         self.left = left

#     def __str__(self):
#         return str(self.val)
    
# if __name__ == "__main__":
#     a = TreeNode(1)
#     b = TreeNode(2)
#     c = TreeNode(3)
#     d = TreeNode(4)
#     e = TreeNode(5)
#     f = TreeNode(6)
#     g = TreeNode(7)

#     a.left = b
#     a.right = c
#     b.left = d
#     b.right = e
#     c.left = f
#     c.right = g

#     print(a)

# def pre_order(node):
#     if not node:
#         return 
    
#     print(node)
#     pre_order(node.left)
#     pre_order(node.right)
# pre_order(a)

# def recurion(n):
#     res = ""
#     if n == 1:
#         return 1
#     elif n == 0:
#         return 0
    
#     return recurion(n - 1) + recurion(n - 2)
    
# print(recurion(5))




# ----------------------------Binary Tree---------------------------------

# class TreeNode:
#     def __init__(self, val):
#         self.left = None
#         self.right = None
#         self.val = val

# class BinaryTree:
#     def __init__(self):
#         self.root = None
    
#     def insert(self, val):
#         if self.root is None:
#             self.root = TreeNode(val)
#         else:
#             self._insert_recursive(self.root, val)

#     def _insert_recursive(self, node, val):
#         if val < node.val:
#             if node.left is None:
#                 node.left = TreeNode(val)
#             else:
#                 self._insert_recursive(node.left, val)
#         else:
#             if node.right is None:
#                 node.right = TreeNode(val)
#             else:
#                 self._insert_recursive(node.right, val)

#     def preorder_traversal(self, node):
#         if node:
#             print(node.val, end="-->")
#             self.preorder_traversal(node.left)
#             self.preorder_traversal(node.right)

#     def postorder_traversal(self, node):
#         if node:
#             self.postorder_traversal(node.left)
#             self.postorder_traversal(node.right)
#             print(node.val, end="-->")
    
#     def search(self, node, val):
#         if node is None or node.val == val:
#             return node
#         if val < node.val:
#             return self.search(node.left, val)
#         return self.search(node.right, val)

#     def dfs(self):
#         if not self.root:
#             return -1
#         stack = [self.root]
#         n = 0
#         while stack:
#             node = stack.pop()
#             print(node.val, end="-->")
#             if node.right: 
#                 n += 1
#                 stack.append(node.right)
#             if node.left:
#                 n += 1
#                 stack.append(node.left)

#     def diameter(self, root, res):
#         if root is None:
#             return 0
        
#         l = self.diameter(root.left, res)
#         r = self.diameter(root.right, res)
#         res[0] = max(res[0], l + r + 1)
#         return 1 + max(l, r)

#     #           10
#     #     5           15
#     # 2       7   12      20

# if __name__ == "__main__":
#     bt = BinaryTree()
#     bt.insert(10)
#     bt.insert(5)
#     bt.insert(15)
#     bt.insert(2)
#     bt.insert(7)
#     bt.insert(12)
#     bt.insert(20)

#     bt.dfs()    
# bt.preorder_traversal(bt.root)

#-------------------------------------------------------------------------------------------------
#------------------------------Recursion-------------------------
# 0, 1, 1, 2, 3, 5, 8, 13, 21
# def recursion(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         l = recursion(n - 1)
#         print("left ", l)
#         r = recursion(n - 2)      
#         print("right ", r)
#         return l + r
    
# print(recursion(8))

# def recursion_add(a, b):
#     if a == 0:
#         return b
    
#     return recursion_add(a - 1, b + 1)

# add = recursion_add(3,4)
# print(add)

#-------------------------------------------------------------------

# def sum_n(n):
#     if n == 0:
#         return 0
    
#     return n + sum_n(n - 1)   

# print(sum_n(5))

#------------------------------------------------------

# class TreeNode:
#     def __init__(self, val):
#         self.left = None
#         self.right = None
#         self.val = val

# class BinaryTree:
#     def __init__(self):
#         self.root = None

#     def insert(self, val):
#         if self.root is None: 
#             self.root = TreeNode(val)
#         else:
#             self.insert_recursively(self.root,val)

#     def insert_recursively(self, root, val):
#         if val < root.val:
#             if root.left is None:
#                 root.left = TreeNode(val)
#             else:
#                 self.insert_recursively(root.left, val)
#         else:
#             if root.right is None:
#                 root.right = TreeNode(val)
#             else:
#                 self.insert_ecursively(root.right, val)

#     def pre_order_traversal(self, node, res:list):
#         self.res = res
#         if self.root is None:
#             return None

#         if node:
#             res.append(node.val)
#             print(node.val, end="->")
#             self.pre_order_traversal(node.left, self.res)
#             self.pre_order_traversal(node.right, self.res)

# if __name__ == "__main__":
#     bt_input = []
#     bt = BinaryTree()
#     bt.insert(5)
#     bt.insert(8)
#     bt.insert(2)
#     bt.pre_order_traversal(bt.root, bt_input)
#     print(bt_input)
#------------------------Subset------------------------------

# def main(nums):
#     res = []
#     def backtrack(subset, i):
#         if i >= len(nums):
#             res.append(subset.copy())
#             return 
        
#         subset.append(nums[i])
#         backtrack(subset, i + 1)
        
#         subset.pop()
#         backtrack(subset, i + 1)

#     backtrack([], 0)
#     return res


# if __name__ == "__main__":
#     subset = [1,2,3]
#     print(main(subset))

#---------------------Recursive Backtracking--------------------------------

#Q1. Write a program to convert integer to word 
# Difficulty Level: Hard
# Input: 1234
# Output: One Thousand Two Hundred Thirty Four

# def main(n):
#     pass


# if __name__ == "__main__":
#     n = 1234
#     print(main(n))