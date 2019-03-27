class Node:

    def __init__(self, v):
        self.value = v
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.leng = 0

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

    def clean(self):
        self.__init__()
        pass # здесь будет ваш код

    def len(self):
        self.leng =0
        if(self.head == None):
            return
        node = self.head
        while node.next is not None:
            node = node.next
            self.leng +=1
        return self.leng+1 # здесь будет ваш код

    def n_value(self):
        if(self.head == None):
            return
        node = self.head
        return node.value
s_list_1 = LinkedList()
s_list_2 = LinkedList()
s_sum_list = LinkedList()


for i in range(10):
    s_list_1.add_in_tail(Node(6))
    s_list_2.add_in_tail(Node(5))

s_list_1.print_all_nodes()
s_list_2.print_all_nodes()

if (s_list_1.len() == s_list_2.len()):
    for i in range(s_list_1.len()):
        m = s_list_1.n_value() + s_list_2.n_value()
        s_sum_list.add_in_tail(Node(m))

        
s_sum_list.print_all_nodes()