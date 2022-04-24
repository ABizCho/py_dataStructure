MAX_QSIZE = 10 # 큐사이즈 지정

class CircularQueue : 
    def __init__( self ) :
        self.front = 0
        self.rear = 0
        self.items = [None] * MAX_QSIZE # NONE*크기 로 초기화시킴
        
    def isEmpty( self ) :
        return self.front == self.rear
    def isFull(self ) : 
        return self.front == (self.rear + 1) % MAX_QSIZE 
    def clear( self ) : 
        self.front = self.rear
        
    def enqueue( self, items ):             
        if not self.isFull():               # 포화상태가 아니면
            self.rear = (self.rear +1) % MAX_QSIZE
            self.items[self.rear] = items
            
    def dequeue( self ):
        if not self.isEmpty():
            self.front = (self.front + 1) % MAX_QSIZE
            return self.items[self.front]
        
    def peek( self ) :
        if not self.isEmpty():
            self.front = (self.front+1 ) % MAX_QSIZE
            return self.items[self.front]
        
    def peek( self ) :
        if not self.isEmpty():
            return self.items[(self.front + 1) % MAX_QSIZE]
    
    def size( self ) :
        return ( self.rear - self.front )
    
    def display ( self ):
        out = []
        if self.front < self.rear : 
            out = self.items[self.front+1: self.rear + 1 ]
            
        else :
            out = self.items[self.front + 1 : MAX_QSIZE ] + self.items[0:self.rear+1]
        print('[f=%s,r=%d] ==> ' %(self.front, self.rear), out )
                
#+=====================테스트 코드

q = CircularQueue()    # 원형 큐 만들기 ( MAX_QSIZE = 10 )

for i in range(8) : q.enqueue(i)    # 0, 1 , ... 7 삽입
q.display()
for i in range(5) : q.dequeue()
q.display()
for i in range(8,14): q.enqueue(i)  # 8,9, ... 13 :  (f=5, r=4) 포화상태 도달
q.display()         