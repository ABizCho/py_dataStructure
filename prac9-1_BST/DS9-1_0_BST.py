'''
BST : 이진탐색트리 

    효율적인 탐색을 위한 트리기반의 자료구조
   
    - 삽입, 삭제, 탐색 : O(logn)    
'''

# 노드의 구조 
    # 하나의 엔트리, (키 , 값)의 형태
    
class BSTNode :# 이진탐색트리를 위한 노드 클래스
    
    # 생성자 : key, value 를 받음  
    def __init__(self, key, value):     
        self.key = key                  # 키 (key)                
        self.value = value              # 값 (value)    -    값을 배열로 매치시킬 수 있을 것
        self.left  = None               # 왼쪽 자식에 대한 링크
        self.right = None               # 오른쪽 자식에 대한 링크
        
    
    # # BST의 탐색 연산 ( 순환 )
    # def search_bst(n, key) :
    #     if n == None :
    #         return None
        
    #     elif key == n.key :
    #         return n
        
    #     elif key < n.key :
    #         return search_bst(n.left, key)

    #     else :
    #         return search_bst(n.right, key)
    
    # BST의 키 탐색  ( 반복 )
    def search_bst(n, key) :
        while n != None : 
            if key == n.key : 
                return n
            
            elif key < n.key :
                n = n.left
            
            else :
                n = n.right
        return None
    
    # Max 탐색 
        # BST의 최대 키는 가장 오른쪽 노드
    def search_max_bst(n) :
        while n != None and n.right != None :
            n = n.right
        return n
    # Min 탐색
        # BST의 최소 키는 가장 왼쪽 노드
    def search_min_bst(n) :
        while n != None and n.left != None :
            n = n.left
        return n
    
    # 삽입 연산
        # 탐색에 실패한 위치 -> 노드를 삽입할 위치 
    def  insert_bst(r, n) :
        if n.key < r.key :
            if r.left is None :
                r.left = n
                return True
            else :
                return insert_bst(r.left, n)