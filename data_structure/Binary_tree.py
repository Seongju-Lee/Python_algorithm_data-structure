
# # 노드 클래스 생성
class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class NodeMgmt:

    # 생성자
    def __init__(self, head):
        self.head = head

    # 데이터 삽입 메소드
    def insert(self, value):
        self.current_node = self.head # 순회할 노드를 head로 지정

        while True:
            if value < self.current_node.value: # 넣을 값이 더 작을 경우
                if self.current_node.left: # 현재 노드의 왼쪽이 존재할 경우
                    self.current_node = self.current_node.left # 더 작은 값으로 바꿔줌
                else:
                    self.current_node.left = Node(value)
                    break
            
            else:       # 넣을 값이 더 클 경우
                if self.current_node.right:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(value)
                    break

    # 데이터 검색 메소드
    def search(self, value):
        
        self.current_node = self.head  # 순회하기 위한 노드 지정
        
        while self.current_node:
            if self.current_node.value == value: # 데이터를 트리구조에서 찾았을 경우
                return True
            elif value < self.current_node.value:
                self.current_node = self.current_node.left
            else:
                self.current_node = self.current_node.right
            
        print('Not found data:', str(value))


# 코드 확인
head = Node(1)
bst = NodeMgmt(head)

bst.insert(2)
bst.insert(3)
bst.insert(4)
bst.insert(0)
bst.insert(9)
bst.insert(8)

bst.search(21)