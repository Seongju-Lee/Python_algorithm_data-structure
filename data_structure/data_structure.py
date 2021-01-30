# # 혼자 연습 파일

# # Linked_List 삽입 구현

class Node:     # 하나의 노드 구현 클래스

    def __init__(self, data, next = None):
        self.data = data
        self.next = next
    
class NodeManage:

    def __init__(self, data): # 처음 생성 할때 사용.
        self.head = Node(data)
        

    def add(self, data): # 링크드 리스트 데이터 추가 메소드
        
        if self.head == None:
            self.head = Node(data)
        else:
            temp_node = self.head
            while temp_node.next:
                temp_node = temp_node.next
            
            temp_node.next = Node(data)

    def desc(self): # 링크드 리스트에 연결된 데이터 확인 메소드
        node = self.head
        while node:
            print(node.data)
            node = node.next

link = NodeManage(1)

for i in range(2,11):
    link.add(i)

link.desc()

