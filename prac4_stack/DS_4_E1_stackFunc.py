'''
DS_4_1

스택 자료구조 
함수형 구현
'''
top = []       #스택의 데이터 : 항목을 위한 공백 리스트

def isEmpty():
    return len(top) == 0
def push(item):
    top.append(item)
def pop():
    if not isEmpty():
        return top.pop(-1)
def peek():
    if not isEmpty():
        return top[-1]
def size(): return len(top)
def clear():
    global top
    top = []