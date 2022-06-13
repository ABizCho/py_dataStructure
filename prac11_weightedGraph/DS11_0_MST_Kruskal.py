'''
Kruskal

그래프로부터 MST(최소 신장 트리)를 구하는 알고리즘에는
그리디 기반의 'Kruskal'과 'Prim' 알고리즘이 있다.

여기서 Kruskal알고리즘은 그래프상 가중치에 대해 오름차순 정렬을 실시하며, (간선의 가중치에 대한 오름차순 정렬을 전제로 하며, 이것이 시간복잡도의 대부분을 차지한다. 따라서 O(eloge))

이를 기반으로 가중치가 작은 간선들을 차례로 선택하여 최소신장트리간선SET에 UNION하되
간선을 집합에 추가하기 전, FIND함수를 통해 기존 집합과 새로 편입될 간선후보 가 합쳐질 때 CYCLE이 발생하는지 확인하고
만일 Cycle이 발생한다면 해당 간선 후보는 집합에 추가하지 않는 과정을 거친다. 이를 통틀어 UNION-FIND 과정이라고 통칭한다.

트리의 특성 상 노드의 개수가 n이라고 할 때, 간선의 수는 n-1개라는 규칙이 있으므로 MST간선SET에 n-1개의 간선이 삽입된다면 종료조건이 충족된다. 

'''

# 0. Kruskal 알고리즘을 위한 기반작업 : union-find 구현
  # init_set(nSets)함수, find(id)함수, union(s1,s2)함수 정의
    
parent = []                     # 모든 개별 노드에 대한 부모노드 인덱스 선언
set_size = 0                    # 전체 집합의 개수 선언

    # 0.1 집합의 초기화 함수 : O(n)의 시간복잡도
def init_set(nSets):            
    global set_size, parent     # 전역에서 선언된 변수를 해당 local Scope내에서 사용(변경)하기 위한 global 선언
    set_size = nSets;           # 집합의 개수
    for i in range(nSets):      # 모든 집합에 대해 : 각각이 고유의 집합(= 부모가 -1)
        parent.append(-1)

    # 0.2 find(id) 함수 : 크루스칼 내 cycle 판별에 활용
def find(id) :                  # input으로 받은 id의 정점이 속한 집합의 대표번호(루트id) 탐색
    while (parent[id] >= 0 ) :  # 해당 id노드의 부모가 '0보다 크거나 같다면'(= 부모노드 인덱스가 아니라면 : init_set참조)
        id = parent[id]             # : 현재 노드의 부모노드의 id를 새로운 타겟id로 갱신(다음스텝 반복을 위한)
    return id;                  # 직전 시행한 반복의 부모노드 id가 -1로 반복이 종료되었다면 현재 갱신된 노드id가 input으로 받은 id노드가 속한 집합의 root노드id이므로 반환

    # 0.3 union(s1,s2) 함수 : 두개의 집합에 대한 합집합 수행 : 크루스칼 내 MSTSET에 새로운 EDGE를 추가할 때 사용됨
        # 매개변수 s1, s2는 각 s1,s2 집합의 root노드의 index
def union(s1, s2) :
    global set_size             # global scope에서 선언한 set_size(전체 집합의 개수를) 해당 local scope에서  사용하기 위한 global 선언
    parent[s1] = s2             # s2에 s1을 병합시킴 ( s1집합의 부모노드 인덱스를 저장한 배열에, s2 집합의 루트노드 인덱스 값을 삽입하였으므로 s1은 s2에 종속됨)
    
    
# 1. Kruskal의 MST 알고리즘
def MSTKruskal(vertex, adj):    # 매개변수: 정점리스트, 인접행렬
    vsize = len(vertex)         # vsize 선언: 그래프 정점의 개수 저장 
    init_set(vsize)             # init_set()의 nSets 매개변수에 그래프 정점의 개수를 인자로 넣어, 처음 N개의 개별 노드들이 각각 고유의 집합으로 존재하도록 초기화시킴
    eList = []                  # eList : 간선 리스트 선언
    
    for i in range(vsize-1) :   # 0부터 n-1 반복 (= 모든 노드에 대해 반복)
        for j in range(i+1, vsize) : # 현재 i노드의 인덱스 직후 노드부터 마지막 노드까지 반복하여 j로 선택
            if adj[i][j] != None :   # 노드i와 j의 간선 가중치가 None이 아니라면 (= i와j가 인접노드로 직접 연결되어 있다면)
                eList.append( (i,j,adj[i][j]) ) # (v1, v2, 간선가중치) 의 튜플을 구성하여 edgeList에 저장
                
    # 간선 리스트를 가중치의 오름차순으로 정렬: 람다함수 사용
        # = O(eloge) = 모든 엣지를 대상으로 하는 정렬 알고리즘이 Kruskal 시간복잡도의 대부분이다.
    eList.sort(key= lambda e : e[2], reverse= True) 
    
    edgeAccepted = 0                    # 트리의 엣지 수 규칙만큼 허용될 수 있는 edge수 판별을 위한 변수 초기화
    while (edgeAccepted < vsize -1) :   # 트리의 성질 규칙에 따라, '엣지수 = 정점수-1' 규칙이 충족될 만큼 반복하고 종료하도록 조건
        e = eList.pop(-1)               # 현재 cycle을 판별해야할 두 정점이 속한 집합의 root노드 번호를 find로 각각 반환받음
        uset = find(e[0])
        vset = find(e[1])
        
        if uset != vset :               # 직전에서 얻은 u와 v 집합의 루트노드 번호가 다르면 다른 집합의 원소라는 결론, 만일 그렇다면 union 실시
            print('간선 추가 : (%s, %s, %d)'
                  %(vertex[e[0]], vertex[e[1]], e[2]))
            union(uset, vset)
            edgeAccepted += 1   # 다음 스텝 반복 전 종료조건 판별을 위한 현재 edge 수 갱신
            


'''테스트코드'''
vertex = ['A','B','C']
weight = [ [ None, 29, None],
           [ 29, None, 16],
           [ None, 16, None] ]

print('MST By Kruskal Algorithm')
MSTKruskal(vertex, weight)