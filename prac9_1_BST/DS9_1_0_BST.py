'''
BST : 이진탐색트리 

    효율적인 탐색을 위한 트리기반의 자료구조
   
    - 삽입, 삭제, 탐색 : O(logn)    
    
    # 코드 참고 : https://skeo131.tistory.com/163?category=420274, 파이썬으로 쉽게 풀어쓴 자료구조 
'''

'''노드 클래스, BST의 단위 데이터로 사용'''
    # 하나의 엔트리, (키 , 값)의 형태 
class BSTNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.list = [{수량:10,주문타입:매도},{수량},{ㅇㅇㅇ}] # 큐 

def search_bst(n, key):
    if n is None:
        return None
    elif n.key == key:
        return n
    elif n.key < key:
        return search_bst(n.right, key)
    else:
        return search_bst(n.left, key)

def search_bst_iter(n, key):
    while n is not None:
        if n.key == key:
            return n
        elif key < n.key:
            n = n.left
        else:
            n = n.right
    return None

def search_value_bst(n, value):
    if n is None:
        return None

    if n.value == value:
        return n
    res = search_value_bst(n.left, value)
    if not res:
        return res
    else:
        return search_value_bst(n.right, value)

def search_bst_max(n):
    while n is not None and n.right is not None:
        n = n.right
    return n

def search_bst_min(n):
    while n is not None and n.left is not None:
        n = n.left
    return n

def insert_bst(r, n):
    if n.key < r.key:
        if r.left is None:
            r.left = n
            return True
        else:
            return insert_bst(r.left, n)
    elif n.key > r.key:
        if r.right is None:
            r.right = n
            return True
        else:
            return insert_bst(r.right, n)
    else:
        return False

# 단말 노트의 삭제
def delete_bst_case1(parent, node, root):
    if parent is None:
        root = None
    else:
        if parent.right is node:
            parent.right = None
        else:
            parent.left = None

    return root

# 자식이 한 개 있는 노드의 삭제
def delete_bst_case2(parent, node, root):
    if node.left is not None:
        child = node.left
    else:
        child = node.right

    if root == node:
        root = child
    else:
        if parent.left is node:
            parent.left = child
        else:
            parent.right = child
    
    return root

# 자식이 두 개 있는 노드의 삭제
def delete_bst_case3(parent, node, root):
    succp = node
    succ = node.right
    while succ.left is not None:
        succp = succ
        succ = succ.left

    if succp.left is succ:
        succp.left = succ.right
    else:
        succp.right = succ.right
    
    node.key = succ.key
    node.value = succ.value
    node = succ

# 모든 경우에 대한 삭제 연산
from typing import *
def delete_bst(root : BSTNode, key):
    if root == None:
        return None
    
    parent = None
    node = root
    while node is not None and node.key != key:
        parent = node
        if node.key < key:
            node = node.right
        else:
            node = node.left

    if node is None:
        return None
    elif node.left is None and node.right is None:
        root = delete_bst_case1(parent, node, root)
    elif node.left is None or node.right is None:
        root = delete_bst_case2(parent, node, root)
    else:
        root = delete_bst_case3(parent, node, root)

    return root

def display(n):
    if n is None:
        return

    display(n.left)
    print(n.key)
    display(n.right)

# for testing
root = BSTNode(35, None)
insert_bst(root, BSTNode(18, None))
insert_bst(root, BSTNode(7, None))
insert_bst(root, BSTNode(3, None))
insert_bst(root, BSTNode(12, None))
insert_bst(root, BSTNode(68, None))
insert_bst(root, BSTNode(26, None))
insert_bst(root, BSTNode(22, None))
insert_bst(root, BSTNode(30, None))
insert_bst(root, BSTNode(90, None))

display(root)
delete_bst(root, 18)
print()
display(root)
            

