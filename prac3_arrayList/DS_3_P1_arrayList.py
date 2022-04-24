'''
DS_3_P1
ArrayList

    리스트 자료구조를 배열구조로 구현하자
    아래에 명시한 리스트 추상자료형(ADT)을 클래스 방법을 통해 실제 자료구조로 구현해보기

======
    
        * 리스트 (광의적) : 선형 자료구조 중 가장 일반적인 자료구조
            
            List = [ Array , Linked List ]
            
                - Array : 탐색에 유리 
                    메모리상에 같은 타입의 자료가 연속적으로 저장된다.
                    
                    # 특징 
                            - 논리적 저장순서와 물리적 저장순서가 일치한다.
                            - 제한적인 메모리 크기 => 꽉찰경우 오버헤드 발생하여 비효율
                            - 탐색이 잦은 경우 Array를 사용하면 좋다.
                    
                    # 장점 : 
                        정렬되어 있지 않다면 탐색에 O(n) 시간이 걸린다.
                        정렬되어 있다면, 이진탐색을 이용(인덱스를 통해), O(logn) ~ O(1) 시간까지 단축. 
                    
                    # 단점 : 
                        But, 정렬을 위한 '삽입 / 삭제' 를 위해 배열을 한칸씩 밀거나,
                        당기는데에 오버헤드가 발생한다. ( 정해진 메모리크기가 제한되어 있기 때문에 )
                    
                - Linked List : 삽입/삭제에 유리 :: 맨앞,맨뒤 위치 삽입/삭제 연산시 O(1)로 단축
                
                    # 특징
                            - 논리적 저장순서와 물리적 저장순서 불일치
                            - 데이터를 추가할 때마다 동적으로 크기 증가
                            - 원소 검색 시 첫번째 노드 ~ 마지막 노드 까지 일일이 확인하기 때문에 O(n)의 시간복잡도
                            - 삽입 / 삭제 연산 시, (1)원소를 검색 (2) 삭제 / 삽입 실행하므로 O(n)의 시간복잡도
                            - 맨 앞 or 맨 뒤 위치에 삽입/삭제 시 O(1)의 시간복잡도
                            - 즉, 삽입/삭제 가 잦은 경우 Linked List가 유리하다.
                            
                    연속된 메모리 공간을 사용하지 않으며 노드간의 연속적 참조로 순서가 연결된다는 특징이, 배열과의 차이점인 리스트타입이다.
                    
                    리스트는 노드단위로 저장되며, 하나의 노드는 [ 데이터를 저장하는 공간 / 다음 노드를 가르키는 참조값 저장 공간 ] 으로 구성되며,
                    리스트 형태로 모든 노드가 연결되어 있는 구조이다.
                    
                    # 단점 : 
                        정렬되어 있지 않다면, 
                            - '탐색' 에 O(n)의 시간이
                            - '삽입' 에 O(1)의 시간이
                            - '삭제' 에 O(n)의 시간이 걸린다.
                            
                        정렬되어야 한다면,
                            - '탐색','삽입','삭제' 에 모두 동일하게 O(n) 의 시간이 걸리므로,
                               Array에 비해 시간복잡도 상 비효율적이다.
                               
                    # 비교우위 : 삽입/삭제 시  오버헤드가 발생할 걱정이 없다. (why? : 정해진 크기가 없고 동적으로 크기를 늘릴 수 있기 때문에 )
                    
ref : 
        - 윤성우의 열혈 자료구조
        - 이것이 코딩테스트다 with Python
        - 쉽게 풀어쓴 코딩테스트 ( 파이썬 )
        - Array & Linked List : https://grepsean.github.io/Algorithms-and-Data-Structures-with-Python-3/ 
        - Linked List : https://velog.io/@gillog/%EC%97%B0%EA%B2%B0-%EB%A6%AC%EC%8A%A4%ED%8A%B8Linked-List
======

            
'''

# ArrayList 자료구조를 class로 구현
class ArrayList :
    def __init__( self ) :
        self.items = []
        
    def insert( self, pos, elem ) :
        tempL = self.items[pos:]    
        self.items = self.items[:pos]   
        self.items.append(elem)
        self.items = self.items + tempL
        
    def delete( self, pos ) :
        return self.items.remove(self.items[pos])
    def isEmpty(self) :
        if len(self.items) == 0 :
            return True
        else : 
            return False
    def getEntry( self, pos ) :
        return self.items[pos]
    def size( self ) :
        return len(self.items)
    def find( self, item ) :
        return self.items.index(item)
    def replace( self, pos, item ) :
        self.items[pos] = item
    def sort( self ) :
        self.items.sort()
    def merge(self, lst) :
        self.items += lst
    def clear( self ) :
        self.items = []
    def display( self, str = '출력' ):
        print(str,self.items)


'''
test 
'''
s = ArrayList()

s.display('파이썬 리스트로 구현한 리스트 테스트: ')
s.insert(0, 10)
s.insert(0, 15)
s.insert(1, 20)
s.insert(1, 30)
s.insert(s.size(), 40)
s.insert(2, 50)
s.display("파이썬 리스트로 구현한 List(삽입x5): ")
s.sort()
s.display("파이썬 리스트로 구현한 List(정렬후): ")
s.replace(2, 90)
s.display("파이썬 리스트로 구현한 List(교체x1): ")

print("find 90 pos: ", s.find(90))
print("find 15 pos: ", s.find(15))

s.delete(2);	s.delete(s.size() - 1);	s.delete(0)
s.display("파이썬 리스트로 구현한 List(삭제x3): ")
lst = [ 1, 2, 3 ]
s.merge(lst)
s.display("파이썬 리스트로 구현한 List(병합+3): ")
s.clear()
s.display("파이썬 리스트로 구현한 List(정리후): ")
