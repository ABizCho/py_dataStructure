class TNODE:
    def __init__ (self, elem, left=None, right=None):
        self.data = elem
        self.left = left
        self.right = right
        
def calc_height(n) :
    if n is None :
        return 0
        
    hLeft = calc_height(n.left)
    hRight = calc_height(n.right)
        
    if(hLeft > hRight) :
        return hLeft + 1

    else :
        return hRight + 1
        
# P8.4 ###################

def checkBalanced(p) :
	if p == None : return True

	diff = calc_height(p.left) - calc_height(p.right)
	if diff < -1 or diff > 1 :
		return False

	if not checkBalanced(p.left):
		return False
	return checkBalanced(p.right)

def is_balanced(root) :
	ret = checkBalanced(root);
	if ret==False : print(" 불균형적인 트리입니다.")
	else : print(" 균형잡힌 트리입니다."); return ret

#P8.5 ###################
def calcPathLength(p, level) :
	if p == None: return 0

	llen = calcPathLength(p.left, level + 1)
	rlen = calcPathLength(p.right, level + 1)
	return llen + rlen + level

def path_length(root) :
	len = calcPathLength(root, 0)
	print(" 전체 경로의 길이는 %d입니다." % len)