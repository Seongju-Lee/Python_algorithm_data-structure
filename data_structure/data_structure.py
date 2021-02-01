# 혼자 연습 파일

# Linked_List 삽입, 삭제 구현

class Node:     # 하나의 노드 구현 클래스

    def __init__(self, data, next = None):
        self.data = data
        self.next = next
    
class NodeManage:

    def __init__(self, data): # 처음 생성 할때 사용.
        self.head = Node(data)
        

    def add(self, data): # 링크드 리스트 데이터 추가 메소드
        
        if self.head == None: # __init__에서 받아온 헤드가 없을 때 사용 -> 사용될 리가 없음
            self.head = Node(data)
        else:                   # 새로운 노드를 추가할 때 사용. head값은 고정 되어 있는 것이고, 그 head를 새로운 변수에 담아 계속하여 탐색 진행
            temp_node = self.head
            while temp_node.next:
                temp_node = temp_node.next
            
            temp_node.next = Node(data)         # 노드의 다음이 None일 때, next에 새롭게 추가한 노드를 가르키도록 설정.

    def desc(self): # 링크드 리스트에 연결된 데이터 확인 메소드
        node = self.head        # head를 새로운 변수에 넣어줌.
        while node:             # 다음 주소가 들어있는 새로운 변수가 None이 나오기 전까지는 계속하여 데이터 출력.
            print(node.data)
            node = node.next

    
    def delete(self, data): # 데이터 삭제 메소드
        
        if self.head == None:
            print("해당 데이터를 가진 노드가 없습니다.")
        
        
        if self.head.data == data: # 해당 데이터를 가진 노드가 첫 번째 노드일때
            
            temp = self.head
            self.head = self.head.next

            del(temp)

        else: # 해당 데이터가 중간이거나 마지막에 존재하는 노드인 경우
            temp_node = self.head

            while temp_node.next:
                
                if temp_node.next.data == data:
                    del_node = temp_node.next
                    temp_node.next = temp_node.next.next

                    del(del_node)
                else:
                    temp_node = temp_node.next


link = NodeManage(1)

for i in range(2,11):
    link.add(i)

link.desc()

print('\n\n첫번째 노드 제거 후 ')
link.delete(1)
link.desc()

print('\n\n중간 노드 제거 후 ')
link.delete(5)
link.desc()

print('\n\n마지막 노드 제거 후 ')
link.delete(10)
link.desc()



############################

#  Double_Linked_List 구현

