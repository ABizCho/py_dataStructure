'''
증권 거래 시스템은 
탐색,삽입,삭제,정렬에 대해 모두 안정적이고 높은 효율을 보장해야 한다.

특히 매수주문과 매도주문 양 사이드의 최극단에 있는 주문끼리 만날 시,
곧장 거래체결을 성사시켜 양쪽의 주문을 추출해야하므로, 최대값 및 최소값의 탐색이 그 중 특히 중요하다고 생각한다.
따라서, 최대 최소의 탐색에 특화된 힙의 우선순위 큐를 사용하여 구현하고자 하였으나, 힙은 '느슨한' 정렬상태를 유지하므로
삽입 삭제 또한 매우 빈번하게 일어나는 해당 시스템에서 정렬에 따른 비효율이 발생할 수 있다고 판단하였다.

이런 문제를 해결하고자 최근에 배운 이진탐색트리맵을 후보로 검토해보았으나, BST의 정렬 유지를 위해 주문 가격을 키로 고려한다면 반드시 중복키가 발생 할텐데
중복 키를 고려할 시 발생하는 비효율 문제로 이 또한 보류하기로 하였다.

그렇게 나온 대안이 '이진트리 + 연결리스트' 구조이다. 

    # Binary Tree + Linked List
        - 중복키 문제 해결 가능
        - 이진트리의 Node에 중복키들을 저장할 연결리스트를 준비
        - BT에서 중복 노드에 도달 시, 연결리스트의 순차적 접근으로 FindFisrt/FindNext 구현 가능
        
        구현 방법 계획 
            - Binary Tree의 노드를 연결리스트로 구현
            - 중복 키 노드 삽입 시, 기존에 존재하는 해당 키를 가진 노드(연결리스트)의 오른쪽으로 붙임
            - 탐색 시, 중복 키 노드의 연결리스트 상 순차탐색 구현
'''


'''1. circular queue by linked list '''
# Python3 program for insertion and  
# deletion in Circular Queue  
  
# Structure of a Node  
class Node: 
    def __init__(self): 
        self.data = None
        self.link = None
  
class Queue: 
    def __init__(self): 
        self.front = None
        self.rear = None
  
# Function to create Circular queue  
def enQueue(q, value): 
    temp = Node()  
    temp.data = value  
    if (q.front == None):  
        q.front = temp  
    else: 
        q.rear.link = temp  
  
    q.rear = temp  
    q.rear.link = q.front 
  
# Function to delete element from  
# Circular Queue  
def deQueue(q): 
    if (q.front == None): 
        print("Queue is empty")  
        return -999999999999
  
    # If this is the last node to be deleted  
    value = None # Value to be dequeued  
    if (q.front == q.rear): 
        value = q.front.data 
        q.front = None
        q.rear = None
    else: # There are more than one nodes  
        temp = q.front  
        value = temp.data  
        q.front = q.front.link  
        q.rear.link= q.front 
  
    return value  
  
# Function displaying the elements  
# of Circular Queue  
def displayQueue(q): 
    temp = q.front  
    # print("Elements in Circular Queue are: ",  
    #                                end = " ")  
    while (temp.link != q.front): 
        print(temp.data, end = " ")  
        temp = temp.link 
    # print(temp.data) 
    return temp.data
  
# # Driver Code 
# if __name__ == '__main__': 
  
#     # Create a queue and initialize 
#     # front and rear  
#     q = Queue()  
#     q.front = q.rear = None
  
#     # Inserting elements in Circular Queue  
#     enQueue(q, 14)  
#     enQueue(q, 22)  
#     enQueue(q, 6)  
  
#     # Display elements present in  
#     # Circular Queue  
#     displayQueue(q)  
  
#     # Deleting elements from Circular Queue  
#     print("Deleted value = ", deQueue(q))  
#     print("Deleted value = ", deQueue(q))  
  
#     # Remaining elements in Circular Queue  
#     displayQueue(q)  
  
#     enQueue(q, 9)  
#     enQueue(q, 20)  
#     displayQueue(q) 
  



'''2. BST'''

'''
이진탐색트리의 노드에는 
KEY, 매수큐 ,매도큐 가 존재한다.

    - KEY는 가격을 담는다.
    - 매수/매도 타입을 인자로 받아 매수큐,매도큐 를 선택하여 들어간다.
    - 큐는 수량의 값을 갖는다.
'''
class BSTNode:
    def __init__(self, isTypeBuy: bool, key: int, value):
        self.key = key
        self.left = None  
        self.right = None
        self.isTypeBuy = isTypeBuy
        self.value = value
        # # isTypeBuy이 True로 들어왔을 경우 매수 주문으로 판단, 매수데이터에 삽입, Vice versa.
        # if isTypeBuy == True : 
        #     self.value_buy = value
        #     self.value_sell = None
        # elif isTypeBuy == False :
        #     self.value_sell = value
        #     self.value_buy = None
        
        if isTypeBuy == True :
            self.q_value_buy = Queue()
            self.q_value_sell = Queue()
            
            enQueue(self.q_value_buy, value)
            self.q_value_sell.front = self.q_value_sell.rear = None
            
        elif isTypeBuy == False :
            self.q_value_buy = Queue()
            self.q_value_sell = Queue()
            
            enQueue(self.q_value_sell, value)
            self.q_value_buy.front = self.q_value_buy.rear = None


##### 
# 필수 : 탐색 (순환)
def search_bst(n, key):
    if n is None:
        return None
    elif n.key == key:
        return n
    elif n.key < key:
        return search_bst(n.right, key)
    else:
        return search_bst(n.left, key)

# 필수 아님 : 값 탐색
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

# 필수 : 최대값 탐색
def search_bst_max(n):
    while n is not None and n.right is not None:
        n = n.right
    return n
# 필수 : 최소값 탐색
def search_bst_min(n):
    while n is not None and n.left is not None:
        n = n.left
    return n

# 필수 : 삽입
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
    # else:
    #     return False
    
    elif n.key == r.key :   # 중복키를 허용 큐 옆에 연결
        if n.isTypeBuy == True :
            enQueue(r.q_value_buy, n.value)
        else :
            enQueue(r.q_value_sell, n.value)            

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
    # print('가격:',n.key,'  ||   ','매수: ',n.value_buy,'    |   ','매도: ',n.value_sell,end=' \n')
    # print('호가:',n.key,'   |   매수주문:',displayQueue(n.q_value_buy),'     |   매도주문:',displayQueue(n.q_value_sell))
    
    if n.q_value_sell.front == None :
        if n.q_value_buy.front == None :
            print('호가창 비어있음')
        else :
            print('호가:',n.key,'   |   매수주문:',displayQueue(n.q_value_buy))
    
    elif n.q_value_buy.front == None :
        if n.q_value_sell.front == None :
            print('호가창 비어있음')
        else :
            print('호가:',n.key,'   |   매도주문:',displayQueue(n.q_value_sell))
    
    else :
        print('호가:',n.key,'   |   매수주문:',displayQueue(n.q_value_buy),'   |   매도주문:',displayQueue(n.q_value_sell))
        
    display(n.right)

################# 테스트 코드 ####################
### 1000 ~ 1100 사에에서 10의 단위로 호가되는 한 주식의 주문시스템

#Q


#BST
root = BSTNode(key=1000, isTypeBuy=False, value ={'수량':100,'주문자':'성우'})
insert_bst(root, BSTNode(key=1000, isTypeBuy=True, value ={'수량':110,'주문자':'재승'}))

# insert_bst(root, BSTNode(key=1010, isTypeBuy=True, value ={'수량':50,'주문자':'재승'}))
# insert_bst(root, BSTNode(key=1020, isTypeBuy=True, value ={'수량':5,'주문자':'성우'}))
# insert_bst(root, BSTNode(key=1030, isTypeBuy=False, value ={'수량':5,'주문자':'성우'}))

display(root)
            


'''
BST구조

노드 = KEY(가격), 매수큐, 매도큐 -> 
    -> 왜 매수매도를 큐로 하는가? : 매수-매도 가격조건 일치 시, 먼저 들어왔던 주문을 먼저 체결시켜야 하기에 선입선출을 지켜야 함
    
    -> 모든 노드는 고유의 가격을 가지고 있고, 노드 내에 매도큐와 매수큐가 공존할 수 없다.
            -> 왜 공존할 수 없나? -> 동일가격의 매수매도 주문이 존재할 경우 주문이 체결되어야 하므로 둘중 하나가 체결되어 사라지거나 동일수량일 경우 둘다 소멸해야 함.

'''