  
# #Function to search a node in BST.
# def search(self, node, x):
#     #code here
#     # print("Debug======>",node.data)
#     while True:
#         print(node.data)
#         node = node.right
#     #     if node.data == None:
#     #         break
#     #     if x == node.data:
#     #         return True
            
#     #     elif x > node.data:
#     #         node = node.right
#     #     elif x < node.data:
#     #         node = node.left
    
#     # return False

#     #{ 
# #  Driver Code Starts
# class Node:
#     """ Class Node """
#     def __init__(self, value):
#         self.left = None
#         self.data = value
#         self.right = None

# class Tree:
#     def createNode(self, data):
#         return Node(data)
    
#     def insert(self, node, data):
#         if node is None:
#             return self.createNode(data)
#         else:
#             if data < node.data:
#                 node.left = self.insert(node.left, data)
#             else:
#                 node.right = self.insert(node.right, data)
#             return node

#     def traverseInorder(self, root):
#         if root is not None:
#             print(root.data, end= " ")
#             self.traverseInorder(root.left)
#             self.traverseInorder(root.right)
    
# if __name__=='__main__':
    # t=int(input())
    # for i in range(t):
    #     n=int(input())
    #     arr = input().strip().split()
    #     root = None
    #     tree = Tree()
    #     root = tree.insert(root, int(arr[0]))
    #     for j in range(1, n):
    #         root = tree.insert(root, int(arr[j]))
    #     #tree.traverseInorder(root)
    #     num = int(input())
    #     find = BST()
    #     if find.search(root, num):
    #         print(1)
    #     else:
    #         print(0)
# class Test:
def checkRecord(s: str) -> bool:
        total_ab = 0
        if len(s)<=2:
            if s == 'LL':
                return True
            if s=='AA':
                return False
            return True
        for i in range(0,len(s)):
            if s[i] == 'A':
                total_ab +=1
            if not i == len(s)-1 and i>0:
                if s[i] == 'L' and s[i-1] == 'L' and s[i+1] == 'L':
                    return False

            if total_ab >=2 :
                return False
        
        return True

print(checkRecord("LLPPPLL"))
        