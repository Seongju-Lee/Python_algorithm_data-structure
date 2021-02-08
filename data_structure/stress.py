
class Stress_node:

    def __init__(self, data, next = None):
        
        self.data = data
        self.next = next



class NodeMag:

    def __init__(self, data):
        self.head = Stress_node(data)

    def add(self, data):

        tmp = self.head

        if tmp == None:
            self.head = Stress_node(data)

        else:

            while(tmp.next):
                tmp = tmp.next

            
            tmp.next = Stress_node(data)

    def desc(self):
        tmp = self.head

        while(tmp.next):
            print(tmp.data)
            tmp = tmp.next

        print(tmp.data)


test = NodeMag(1)
for i in range(2,11):

    test.add(i)
test.desc()

