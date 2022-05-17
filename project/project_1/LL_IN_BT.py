# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # head : ListNode / root : ListRoot
    def isSubPath(self, head, root):

        dataList = []
        curListNode = head
        # dataList 배열에 curListNode(head)의 값을 넣는다.
        while curListNode:
            dataList.append(curListNode.val)
            curListNode = curListNode.next
        #print('dataList = ', dataList)

        self.res = False
        # self의 data를 추가하고 빈 배열을 추가한다.
        self.data = []

        # curNode 현재 노드 / curList 현재 리스트
        def helper(curNode, curList):
            # 현재 노드가 None 이라면
            if(curNode == None):
                # self.data 배열안에 curList가 없다면
                if(curList not in self.data):
                    # curList를 self.data 배열 안에 추가한다.
                    self.data.append(curList)
                # 현재 노드가 None 이 아니라면 curList 배열과 curNode.val을 합친다.
                return
            helper(curNode.left, curList+[curNode.val])
            helper(curNode.right, curList+[curNode.val])

        # root에서 처음 시작하는 재귀함수 실행
        helper(root, [])
        #print("end self.data = ", self.data)

        #self.data 배열을 반복해서 하나씩 꺼내본다.
        for data in self.data:
            #print('data = ',data)
            indexes = []
            # data의 배열을 하나씩 꺼내서 본다.
            for i in range(len(data)):
                num = data[i]
                #print('num = ', num)
                # dataList의 첫번째 배열값과 data의 배열값이 같아진다면
                if (num == dataList[0]):
                    # indexes 배열에 index를 추가한다.
                    indexes.append(i)
            #print('indexes = ', indexes)
            # indexes 배열이 비어있다면 for문을 계속해서 반복한다.
            if(indexes == []):
                continue


            tmpLen = len(dataList)
            #print('tmpLen =',tmpLen)

            for idx in indexes:
                if(data[idx:idx+tmpLen] == dataList):
                    #print(data[idx:idx+tmpLen])
                    #print(dataList)
                    return True
        return False