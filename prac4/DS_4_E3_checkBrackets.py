'''
DS_4_P3

스택 자료구조를 이용한 
괄호검사 알고리즘


    * 괄호의 종류 : 대중소 [ ] , { } , ( )
            - { [ ( ) ] } : LIFO원리 적용됨 
    * 조건 : 

        - 왼쪽 괄호의 개수와 오른쪽 괄호의 개수가 같아야 한다.
        - 같은 타입의 괄호에서 왼쪽 괄호가 오른쪽 괄호보다 먼저 나와야 한다.
        - 서로 다른 타입의 괄호 쌍이 서로를 교차하면 안 된다.
        
    * 방법 :

        1. 괄호 쌍 중 왼쪽괄호들은 모두 차례로 스택에 쌓는다.
        2. 파싱 중 오른쪽 괄호를 만나는 시점부터, 쌓아져있는 최상위(Last) item과 순서대로 비교하여 모두 일치하면 OK
    
'''
class Stack :
    def __init__( self ) : 
        self.top = []
        
    
    def isEmpty( self ) : 
        return len( self.top ) == 0
    
    def size( self ):
        return len(self.top)
    
    def clear( self ): 
        self.top = []
    
    def push( self, item ):
        self.top.append(item)
        
    def pop ( self ) :
        if not self.isEmpty():
            return self.top.pop(-1)
        
    def peek( self ):
        if not self.isEmpty():
            return self.top[-1]
        
#---
def checkBrackets(statement):
    stack = Stack()
    for ch in statement :
        if ch in ('{','[','('):
            stack.push(ch)
        
        elif ch in ('}',']',')'):
            if stack.isEmpty():
                return False
            
        else : 
            left = stack.pop()
            if (ch == '}' and left 1= '{') or