'''
DS 3_1
Line editor : 배열을 응용한
'''

class ArrayList:
    def __init__( self ):
        self.items = []
        
    def insert(self, pos, elem) :
        self.itmes.insert(pos, elem)
    def delete(self, pos) :
        self.items.pop(pos)
    def isEmpty( self ) :
        return self.size() == 0
    def getEntery(self, pos) :
        return self.items[pos]
    def size( self ):
        return len(self.items)
    def clear( self ) :
        self.items = []
    def find(self, item) :
        return self.items.index(item)
    def replace(self, pos, elem) :
        self.items[pos] = elem
    def sort(self) :
            



