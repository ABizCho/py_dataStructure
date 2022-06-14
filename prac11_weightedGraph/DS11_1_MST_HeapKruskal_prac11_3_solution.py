class MinHeap :					
    def __init__ (self) :		
        self.heap = []			
        self.heap.append(0)		

    def size(self) : return len(self.heap) - 1	
    def isEmpty(self) : return self.size() == 0	
    def Parent(self, i) : return self.heap[i//2]
    def Left(self, i) : return self.heap[i*2]	
    def Right(self, i) : return self.heap[i*2+1]
    def display(self, msg = '힙 트리: ') :
        print(msg, self.heap[1:])	

    def insert(self, n) :
        self.heap.append(n)		
        i = self.size()			
        while (i != 1 and n < self.Parent(i)): 
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
                if child<self.size() and self.Left(parent)>self.Right(parent):
                    child += 1
                if last <= self.heap[child] :       
                    break;		                    
                self.heap[parent] = self.heap[child]
                parent = child
                child *= 2;

            self.heap[parent] = last	
            self.heap.pop(-1)		    
            return hroot	

parent = []     # 각 노드의 부모노드 인덱스	
set_size = 0    # 전체 집합의 개수	

def init_set(nSets) :
    global set_size, parent 
    set_size = nSets;
    for i in range(nSets):
        parent.append(-1)		# 맨 처음에는 모든 정점이 각각 고유의 집합	

def find(id) :
    while (parent[id] >= 0) :
        id = parent[id];
    return id;

def union(s1, s2) :
    global set_size
    parent[s1] = s2;
    set_size = set_size - 1;


class HNode :			# 힙에 저장할 노드
    def __init__(self, v1, v2, key):
        self.key = key
        self.v1 = v1
        self.v2 = v2
    def __lt__(self, rhs):
        return self.key < rhs.key
    def __le__(self, rhs):
        return self.key <= rhs.key


# kruskal의 최소 비용 신장 트리 프로그램 
def MSTKruskal(vertex, adj):
    edgeAccepted = 0
    heap = MinHeap()
    vsize = len(vertex)
    init_set(vsize)

    for i in range(vsize-1) : 
        for j in range(i+1, vsize) :
            if adj[i][j] != None :
                heap.insert(HNode(i, j, adj[i][j]))

    while (edgeAccepted < vsize - 1) :
        e = heap.delete()
        uset = find(e.v1);
        vset = find(e.v2);

        if (uset != vset) :
            print("간선 추가 : %s - %s (비용:%d)" % (vertex[e.v1], vertex[e.v2], e.key))
            union(uset, vset)
            edgeAccepted += 1
    return


weight = [ [None,	29,		None,	None,	None,   10,		None],
           [29,		None,	16,		None,	None,	None,	15  ],
           [None,	16,		None,	12,		None,	None,	None],
           [None,	None,   12,		None,	22,		None,	18  ],
           [None,	None,	None,   22,		None,	27,		25  ],
           [10,		None,	None,	None,   27,		None,	None],
           [None,   15,		None,   18,		25,		None,	None]]    
vertex =   ['A',    'B',    'C',    'D',    'E',    'F',    'G' ]

print("MST By Kruskal's Algorithm")
MSTKruskal(vertex, weight)

# '''테스트코드'''
# vertex = ['A','B','C']
# weight = [ [ None, 29, None],
#            [ 29, None, 16],
#            [ None, 16, None] ]

# print('MST By Kruskal Algorithm')
# MSTKruskal(vertex, weight)