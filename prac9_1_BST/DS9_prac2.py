
# 숫자들이  들어있는  이진탐색트리를  중위  순회(traversal)하면  정렬된  숫자가  얻어진다. 
    #•       다음  배열에  들어있는  숫자들을  정렬시키는  함수를  작성하시오. 
    #–       배열에  들어  있는  숫자들을  이진탐색트리에  차한  후에  트리를  중위  순회하면서  숫자들을  출력한다. 단, 숫자 들은  중복되지  않는다고  가정

from DS9_1_1_bstMap import *

def testP9_3():
    map = BSTMap()
    data = [11, 3, 4, 1, 56, 5, 6, 2, 98, 32, 23]
    
    print('[삽입연산]:', data)
    for key in data :
        map.insert(key)
    map.display('[중위 순회] :')
