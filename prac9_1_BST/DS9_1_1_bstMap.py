from DS9_1_0_BST import *

'''BST로 구현한 Map(=파이썬의 딕셔너리)'''
class BSTMap:
    def __init__(self):
        self.root = None
    
    def isEmpty(self):
        return self.root == None
    
    def clear(self):
        self.root = None
    
    def size(self):
        def count_node():
            node = self.root
            if node is None:
                return 0
            stack = []
            stack.append(node)
            cnt = 0
            while stack:
                cnt += 1
                if node.left is not None:
                    stack.append(node.left)
                if node.right is not None:
                    stack.append(node.right)
            return cnt
        return count_node()

    def search(self, key):
        return search_bst(self.root, key)
    
    def searchValue(self, value):
        return search_value_bst(self.root, value)
    
    def findMax(self):
        return search_bst_max(self.root)

    def findMin(self):
        return search_bst_min(self.root)

    def insert(self, key, value=None):
        n = BSTNode(key, value)
        if self.isEmpty():
            self.root = n
        else:
            insert_bst(self.root, n)

    def delete(self, key):
        self.root = delete_bst(self.root, key)

    def display(self, msg="BSTMap :"):
        def inorder(n):
            if n.left:
                inorder(n.left)
            print(n.key, end=' ')
            if n.right:
                inorder(n.right)
        
        print(msg, end='')
        inorder(self.root)
        print()
####
map = BSTMap()
data = [35, 18, 7, 26, 12, 3, 68, 22, 30, 99]
print("[삽입 연산] : ", data)
for key in data:
    map.insert(key)
map.display("[중위 순회] : ")