class MinHeap :					
    def __init__ (self) :		
        self.heap = []			
        self.heap.append(0)		
        
    def size(self) : return len(self.heap) - 1	
    def isEmpty(self) : return self.size() == 0	
    def Parent(self, i) : return self.heap[i//2]
    def Left(self, i) : return self.heap[i*2]	
    def Right(self, i) : return self.heap[i*2+1]
    def display(self, msg = '�� �몃━: ') :
        print(msg, self.heap[1:])

    def insert(self, n) :
        self.heap.append(n)		
        i = self.size()			        
        while (i != 1 and n.freq < self.Parent(i).freq): 
            self.heap[i] = self.Parent(i)	   
            i = i // 2			               
        self.heap[i] = n		            	

    def delete(self) :
        parent = 1
        child = 2
        if not self.isEmpty() :
            hroot = self.heap[1]		    
            last = self.heap[self.size()]	
            while (child <= self.size()):	
                if child<self.size() and self.Left(parent).freq>self.Right(parent).freq:
                    child += 1
                if last.freq <= self.heap[child].freq :       
                    break;		                    
                self.heap[parent] = self.heap[child]
                parent = child
                child *= 2;

            self.heap[parent] = last	
            self.heap.pop(-1)		    
            return hroot

''''''
class HuffNode:
    def __init__(self, symbol, freq):
        self.symbol = symbol
        self.freq = freq
        self.left = None
        self.right = None
        self.code = ''
        
    def __str__(self):
        return f"{self.symbol} : {self.freq}"

    def preorder(self):
        print(self.freq, end=" ")

        if (self.left is not None):
            self.left.preorder()
        if (self.right is not None):
            self.right.preorder()


    def inorder(self):
        if (self.left is not None):
            self.left.inorder()

        print(self.freq, end=" ")
        if (self.right is not None):
            self.right.inorder()


''''''
def huffman(n, heap):    
    for _ in range(n - 1):
        e1 = heap.delete()  #p = PQ.get()[1]
        e2 = heap.delete()  #q = PQ.get()[1]
        print("min: ", e1, e2)
        r = HuffNode(' ', e1.freq + e2.freq)
        r.left = e1
        r.right = e2
        
        heap.insert(r)
        print("insert: ", r)
        print("left: ", e1, "right: ", e2)
        
    root = heap.delete()
    return root


##########Driver Code######################

codes = ['E', 'T', 'N', 'I', 'S']
freqs = [15, 12, 8, 6, 4]

heap = MinHeap()

for i in range(len(codes)):
    node = HuffNode(codes[i], freqs[i])
    heap.insert(node)
    #PQ.put((node.freq, node))

#root = huffman(len(codes), PQ)
root = huffman(len(codes), heap)

print("Preorder:", end=" ")
root.preorder()
print("\nInorder:", end=" ")
root.inorder()
print()