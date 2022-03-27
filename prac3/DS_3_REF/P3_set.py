# Set
'''
참고 : https://comdoc.tistory.com/entry/18-%EC%A7%91%ED%95%A9set-ADT-%ED%8C%8C%EC%9D%B4%EC%8D%AC
'''
class Set:				        
    def __init__( self ):		
        self.items = []			

    def size( self ): 			
        return len(self.items)	
    def display(self, msg):		
        print(msg, self.items)	

#    def contains(self, item) :
#       return item in self.items

    def contains(self, item) :
        for i in range(len(self.items)):
            if self.items[i] == item :	
                return True
        return False		

    def insert(self, elem) :
        if elem not in self.items :
           self.items.append(elem)

    def delete(self, elem) :
        if elem in self.items :
           self.items.remove(elem)

    def union( self, setB ):		    
        setC = Set()			        
        setC.items = list(self.items)	
        for elem in setB.items :	    
            if elem not in self.items :	
                setC.items.append(elem)	
        return setC			            

    def intersect( self, setB ):	
        setC = Set()
        for elem in setB.items :	
            if elem in self.items :	
                setC.items.append(elem)	
        return setC

    def difference( self, setB ):	    
        setC = Set()
        for elem in self.items:		    
            if elem not in setB.items:	
                setC.items.append(elem)	
        return setC
    
    def is_propSubset_of(self, setB) :
        isPS = True
        for i in self.items :
            if i not in setB.items:
                isPS = False
        if len(self.items) >= len(setB.items) :
            isPS = False
        return isPS
                
                

setA = Set()
setB = Set()

setA.insert(1)
setA.insert(2)
setA.insert(3)
setA.insert(3)

setB.insert(3)
setB.insert(2)
setB.insert(1)
setB.insert(4)

print( setA.is_propSubset_of(setB))


# setA.insert('휴대폰')
# setA.insert('지갑')
# setA.insert('손수건')
# setA.display('Set A:')

# setB = Set()
# setB .insert('빗')
# setB .insert('파이썬 자료구조')
# setB .insert('야구공')
# setB .insert('지갑')
# setB.display('Set B:')

# setB.insert('빗')
# setA.delete('손수건')
# setA.delete('발수건')
# setA.display('Set A:')
# setB.display('Set B:')

# setA.union(setB).display('A U B:')
# setA.intersect(setB).display('A ^ B:')
# setA.difference(setB).display('A - B:')