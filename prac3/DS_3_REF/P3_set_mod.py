# Set.

'''
참고 : https://comdoc.tistory.com/entry/18-%EC%A7%91%ED%95%A9set-ADT-%ED%8C%8C%EC%9D%B4%EC%8D%AC
'''
class Set:
    def __init__( self ):
        self.items = []

    def size( self ):
        return len(self.items)

    def contains(self, item) :
        for i in range(len(self.items)) :   # len(self.items) -> self.size()
            if self.items[i] == item :
                return True
        return False

    def insert(self, elem) :
        if self.contains(elem) == False :
           self.items.append(elem)

    def delete(self, elem) :
        for i in range(len(self.items)) :
            if self.items[i] == elem :
                self.items.pop(i)
    
    def union( self, setB ):                # C = self U  B
        newSet = Set()
        newSet.items = list(self.items)
        for elem in setB.items :
            if not self.contains(elem) :
                newSet.items.append(elem)
        return newSet

    def intersect( self, setB ):            # C = self ∩ B
        setC = Set()
        for elem in setB.items :
            if self.contains(elem) :
                setC.items.append(elem)
        return setC

    def difference( self, setB ):           # C = self - B
        setC = Set()
        for elem in self.items:
            if not setB.contains(elem) :  # not True = False
                setC.items.append(elem)
        return setC

    def __sub__( self, setB ):           # C = self - B
        return self.difference(setB)

    def isSubsetOf( self, setB ):
        for elem in self.items :
            if elem not in setB : return False
        return True

    def display(self, msg):
        print(msg, self.items)
        
    def is_propSubset_of(self, setB) :
        isPS = True
        for i in self.items :
            if i not in setB.items:
                isPS = False
        if len(self.items) >= len(setB.items) :
            isPS = False
        return isPS

#======================================================================
setA = Set()
setA.insert('휴대폰')
setA.insert('지갑')
setA.insert('손수건')
setA.display('Set A:')

setB = Set()
setB .insert('빗')
setB .insert('파이썬 자료구조')
setB .insert('야구공')
setB .insert('지갑')
setB.display('Set B:')

setB.insert('빗')
setA.delete('손수건')
setA.delete('발수건')
setA.display('Set A:')
setB.display('Set B:')

setA.union(setB).display('A U B:')
setA.intersect(setB).display('A ∩ B:')
setA.difference(setB).display('A - B:')
(setA-setB).display('A - B:')

