'''
Bag Class
'''

class Bag:
    def __init__( self ):
        self.bag = []

    def contains(self, e) :
        return e in self.bag

    def insert(self, e) :
        self.bag.append(e)

    def remove(self, e) :
        self.bag.remove(e)

    def count(self):
        return len(self.bag)


myBag = Bag()
myBag.insert('버즈 프로');    myBag.insert('핸드폰')
myBag.insert('휴대용 모니터');    myBag.insert('노트북')
myBag.insert('자료구조');  myBag.insert('충전기')
print('가방속의 물건:', myBag.bag)

myBag.insert('펜')
myBag.remove('휴대용 모니터')
print('가방속의 물건:', myBag.bag)


