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

from ...prac9_1_BST.DS9_1_0_BST import *

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
keys = [1000, 1010, 1100, 1020, 12, 3, 68, 22, 30, 99]
value = []
print("[삽입 연산] : ", keys)

for key_idx in range(len(keys)):
    map.insert(key = data[key_idx],
               value = value[key_idx])
map.display("[중위 순회] : ")