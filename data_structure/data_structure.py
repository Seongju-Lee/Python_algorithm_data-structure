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
#  양방향으로 연결되어 있어서 노드탐색이 양쪽으로 모두 가능


class Double_Node:

    def __init__(self, data, prev = None, next = None):

        self.data = data
        self.prev = prev
        self.next = next

class NodeMan:

    def __init__(self, data):
        self.head = Double_Node(data)
        self.tail = head

    def insert(self, data):

        if self.head == None: # 방어크드
            self.head = Double_Node(data)
            self.tail = self.head

        else:
            temp = self.head

            while temp.next:
                temp = temp.next
            new = Double_Node(data)
            temp.next = new
            new.prev = temp

            self.tail = new



class Node: # 노드 구현 클래스

    def __init__(self, data, prev = None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class NodeMgmt: # 링크드 리스트 관리

    def __init__(self, data):   # 생성자 
        self.head = Node(data)  # head를 첫 노드로 지정
        self.tail = self.head   # node가 하나인 상태이기 때문에 head와  tail 동일하게 지정

    def insert(self, data):

        if self.head == None:   
            self.head = Node(data)
            self.tail = self.head
        
        else:
            node = self.head    # head를 빈 변수에 하나 지정
            while node.next:    # 다음 노드가 있다면, 다음 노드를 현재 변수로 최신화
                node = node.next
            new = Node(data)    # 다음 노드가 없을 때, 마지막이므로, 새로운 노드를 생성
            node.next = new     # 새로운 노드를 이전 노드의 next로 지정
            new.prev = node     # 새로운 노드의 prev를 이전 노드로 지정

            self.tail = new     # 마지막 노드는 새로 생성한 노드이므로, tail을 new로 지정

    def desc(self):             # head부터 순회하며, 마지막 노드까지 출력하는 메소드
        node = self.head

        while node:
            print(node.data)
            node = node.next


    # 검색을 담당하는 메소드

    def search_from_head(self, data): # head부터 검색

        if self.head == None: # 방어코드
            return False

        node = self.head
        while node:
            if node.data == data:
                return node
            else:
                node = node.next

        return False

    def search_from_tail(self, data): # tail부터 검색

        if self.head == None: # 방어코드
            return False

        node = self.tail
        while node:
            if node.data == data:
                return node
            else:
                node = node.prev

        return False


    # 노드 데이터가 특정 숫자인 노드 앞에 데이터를 추가하는 함수

    def insert_before(self, data, before_data):

        if self.head == None:
            self.head = Node(data)
            return True
        else:
            node = self.tail
            while node.data != before_data:
                node = node.prev
                if node == None:
                    return False
                
            # 특정 노드를 찾았을 때
            new = Node(data)

            before_new = node.prev # 원래 앞에 있던 노드
            before_new.next = new
            
            new.prev = before_new
            new.next = node

            node.prev = new

            return True


    # 노드 데이터가 특정 숫자인 노드 뒤에 데이터를 추가하는 함수

    ### 작성해보기 ###

