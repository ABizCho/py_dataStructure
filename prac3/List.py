'''
파이썬의 리스트인 Array를 이용하여
자료구조 리스트(ADT) 를 구현
'''

items = []
def insert(pos,elem) :
    items.insert(pos, elem)

def delete(pos) :
    return items.pop(pos)

def getEntry(pos):
    return items[pos]

def isEmpty():
    return len(items) == 0

def size(): 
    return len(items)