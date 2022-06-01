#이진탐색트리에서  최대  키와  최소  키를  가진  노드를  탐색하는  함수를  순환구조를  이용하여 구현하시오. (반복구조로  구현한  9.2절의  함수들을  참고)

def search_max_bst_recur(n):
    if n == None or n.right == None : 
        return n
    return search_max_bst_recur(n.right)

def search_min_bst_recur(n) :
    if n == None or n.left == None :
        return n
    return search_min_bst_recur(n.left)