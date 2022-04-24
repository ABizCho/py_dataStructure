# 덱의 구조

스택이나 큐보다 입출력이 자유로운 자료구조

- Deque(덱) 은 double-ended queue 의 줄임말

  - 전단(front)와 후단(rear)에서 모두 삽입과 삭제가 가능한 큐

    ## ADT

          - Deque() : 덱 생성
          - isEmpty()
          - addFront(x) : 항목 x를 덱의 맨 앞에 추가한다.
          - deleteFront()
          .....

# 원형 덱

    - 큐와 데이터는 동일하다
    - 연산은 유사하다
    - 개념은 똑같지만, 반시계방향으로 감소하면서 이동한다.

        -> 큐와 알고리즘이 동일한 연산 :
            addRear(), deleteFront(), getFront(),addRear(),isFull(),size(),clear()

        => 추가될 필요가 있는 연산 : addFront(), deleteRear(), getRear()

    ## 원형 큐를 상속하여 원형 덱 클래스를 구현할 수 있다.
    -> class CiruclarDeque(CircularQueue) : # CircularQueue에서 상속
