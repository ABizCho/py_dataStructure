# BFS 너비우선탐색 ( 큐 응용 )

#
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
#


def BFS() :
    que = CircularQueue()
    
    que.enqueue((0,1))