
class BSTNode :# 이진탐색트리를 위한 노드 클래스
    
    # 생성자 : key, value 를 받음  
    def __init__ (self, key, value):     
        self.key = key                  # 키 (key)                
        self.value = value              # 값 (value)    -    값을 배열로 매치시킬 수 있을 것
        self.left  = None               # 왼쪽 자식에 대한 링크
        self.right = None               # 오른쪽 자식에 대한 링크
        
    
    # 탐색 연산
    def search_bst(n, key) :
        if n == None :
            return None
        
        elif key == n.key :
            return n
        
        elif key < n.key :
            return search_bst(n.left, key)

        else :
            return search_bst(n.right, key)